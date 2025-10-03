from collections.abc import Callable

from jinja2 import BaseLoader, Environment
from typing_extensions import override

from pipelex import log
from pipelex.tools.templating.template_provider_abstract import TemplateProviderAbstract


class Jinja2TemplateLoader(BaseLoader):
    def __init__(self, template_provider: TemplateProviderAbstract) -> None:
        super().__init__()
        self.template_provider = template_provider

    @override
    def get_source(self, environment: Environment, template: str) -> tuple[str, str | None, Callable[[], bool] | None]:
        the_template = self.template_provider.get_template(template_name=template)
        log.debug(f"TemplateLoader.get_source: template='{template}'")
        return the_template, None, None
