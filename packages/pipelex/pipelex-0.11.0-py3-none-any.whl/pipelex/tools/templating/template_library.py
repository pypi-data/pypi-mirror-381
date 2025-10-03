from pathlib import Path
from typing import Any, ClassVar, cast

from jinja2 import TemplateSyntaxError
from pydantic import Field, RootModel, ValidationError
from typing_extensions import override

from pipelex import log
from pipelex.libraries.library_config import LibraryConfig
from pipelex.tools.exceptions import ToolException
from pipelex.tools.misc.file_utils import find_files_in_dir
from pipelex.tools.misc.toml_utils import load_toml_from_path
from pipelex.tools.templating.jinja2_parsing import check_jinja2_parsing
from pipelex.tools.templating.jinja2_template_category import Jinja2TemplateCategory
from pipelex.tools.templating.template_preprocessor import preprocess_template
from pipelex.tools.templating.template_provider_abstract import TemplateNotFoundError, TemplateProviderAbstract
from pipelex.tools.typing.pydantic_utils import format_pydantic_validation_error

TemplateLibraryRoot = dict[str, str]


class TemplateLibraryError(ToolException):
    pass


class TemplateLibrary(TemplateProviderAbstract, RootModel[TemplateLibraryRoot]):
    root: TemplateLibraryRoot = Field(default_factory=dict)
    library_config: ClassVar[LibraryConfig]

    @classmethod
    def make_empty(cls, config_dir_path: str) -> "TemplateLibrary":
        cls.library_config = LibraryConfig(config_dir_path=config_dir_path)
        return cls()

    @override
    def setup(self) -> None:
        templates_dir = Path(__file__).parent / "templates"
        template_toml_paths = find_files_in_dir(dir_path=str(templates_dir), pattern="*.toml", is_recursive=True)
        for template_toml_path in template_toml_paths:
            self._load_from_toml(toml_path=str(template_toml_path))
        self.validate_templates(template_category=Jinja2TemplateCategory.LLM_PROMPT)

    @override
    def teardown(self) -> None:
        self.root = {}

    @override
    def get_template(self, template_name: str) -> str:
        try:
            return self.root[template_name]
        except KeyError as exc:
            msg = f"Template '{template_name}' not found in template library"
            raise TemplateNotFoundError(msg) from exc

    def _set_template(self, template: str, name: str):
        preprocessed_template = preprocess_template(template)
        self.root[name] = preprocessed_template

    def _add_new_template(self, template: str, name: str):
        if name in self.root:
            msg = f"Template '{name}' already exists in the library"
            raise TemplateLibraryError(msg)
        self._set_template(template=template, name=name)

    def _load_from_toml(self, toml_path: str):
        nb_concepts_before = len(self.root)
        library_dict = load_toml_from_path(path=toml_path)
        for start_domain, templates in library_dict.items():
            self._load_from_recursive_dict(domain=start_domain, recursive_dict=templates)
        toml_name = toml_path.split("/")[-1]
        log.debug(f"Loaded {len(self.root) - nb_concepts_before} templates from '{toml_name}'")

    def _load_from_recursive_dict(self, domain: str, recursive_dict: dict[str, Any]):
        for name, obj in recursive_dict.items():
            try:
                if isinstance(obj, str):
                    # it's a template
                    template = obj
                    self._add_new_template(template=template, name=name)
                elif isinstance(obj, dict):
                    # this is not a templae but a subdomain
                    sub_recursive_dict = cast("dict[str, str]", obj)
                    domain = f"{domain}/{name}"
                    self._load_from_recursive_dict(domain=domain, recursive_dict=sub_recursive_dict)
                else:
                    msg = f"Unexpected type for key '{name}' in recursive_dict: {type(obj)}"
                    raise TemplateLibraryError(msg)
            except ValidationError as exc:
                error_msg = format_pydantic_validation_error(exc)
                msg = f"Error loading concept '{name}' of domain '{domain}' because of: {error_msg}"
                raise TemplateLibraryError(msg) from exc

    def validate_templates(self, template_category: Jinja2TemplateCategory):
        for template_name, template in self.root.items():
            try:
                check_jinja2_parsing(
                    jinja2_template_source=template,
                    template_category=template_category,
                )
            except TemplateSyntaxError as exc:
                error_msg = f"Jinja2 syntax error in template '{template_name}': {exc}."
                if template:
                    error_msg += f"\nThe template is:\n{template}"
                else:
                    error_msg += "The template is empty."
                msg = error_msg
                raise TemplateLibraryError(msg) from exc
