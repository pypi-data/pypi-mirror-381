from typing import Any

from typing_extensions import override

from pipelex import log
from pipelex.cogt.exceptions import LLMPromptFactoryError, LLMPromptTemplateInputsError
from pipelex.cogt.image.prompt_image import PromptImage
from pipelex.cogt.llm.llm_prompt import LLMPrompt
from pipelex.cogt.llm.llm_prompt_factory_abstract import LLMPromptFactoryAbstract
from pipelex.cogt.llm.llm_prompt_template_inputs import LLMPromptTemplateInputs
from pipelex.config import get_config
from pipelex.hub import get_template
from pipelex.tools.misc.string_utils import is_none_or_has_text


def make_empty_prompt() -> LLMPrompt:
    return LLMPrompt(
        system_text=None,
        user_text=None,
        user_images=[],
    )


class LLMPromptTemplate(LLMPromptFactoryAbstract):
    proto_prompt: LLMPrompt = make_empty_prompt()
    base_template_inputs: LLMPromptTemplateInputs = LLMPromptTemplateInputs()

    # fields kept for reference and debugging only (they have no effect)
    source_system_template_name: str | None = None
    source_user_template_name: str | None = None

    @override
    async def make_llm_prompt_from_args(
        self,
        **prompt_arguments: Any,
    ) -> LLMPrompt:
        arguments_dict = prompt_arguments.copy()

        # pop the base fields and then use the templating method
        system_text: str | None = arguments_dict.pop("system_text", None)
        user_text: str | None = arguments_dict.pop("user_text", None)
        if not user_text:
            user_text = self.proto_prompt.user_text

        # user_images is Optional here: None means the template is not altering the user_images field
        user_images: list[PromptImage] | None = None
        if "user_images" in arguments_dict:
            user_images = arguments_dict.pop("user_images")
        elif "user_image" in arguments_dict:
            user_images = [arguments_dict.pop("user_image")]
        is_user_images_append: bool | None = arguments_dict.pop("is_user_images_append", None)

        return self.make_llm_prompt(
            system_text=system_text,
            user_text=user_text,
            user_images=user_images,
            is_user_images_append=is_user_images_append,
            template_inputs=LLMPromptTemplateInputs(root=arguments_dict),
        )

    def make_llm_prompt(
        self,
        system_text: str | None = None,
        user_text: str | None = None,
        user_images: list[PromptImage] | None = None,
        is_user_images_append: bool | None = None,
        template_inputs: LLMPromptTemplateInputs | None = None,
    ) -> LLMPrompt:
        if not is_none_or_has_text(system_text):
            if system_text == "":
                log.warning(f"Prompt template system_text should be None or contain text. system_text = '{system_text}'")
            else:
                msg = f"Prompt template system_text should be None or contain text. system_text = '{system_text}'"
                raise LLMPromptTemplateInputsError(msg)
        if not is_none_or_has_text(user_text):
            msg = f"Prompt template user_text should be None or contain text. system_text = '{user_text}'"
            raise LLMPromptTemplateInputsError(msg)

        all_template_inputs = self.base_template_inputs.complemented_by(additional_template_inputs=template_inputs)

        # input variables can override prompt texts

        llm_prompt = self.proto_prompt.model_copy()
        if system_text:
            llm_prompt.system_text = system_text
        if user_text:
            llm_prompt.user_text = user_text
        if user_images:
            if is_user_images_append:
                llm_prompt.user_images.extend(user_images)
            else:
                llm_prompt.user_images = user_images

        # input variables can be applied to prompt texts used as templates
        if llm_prompt.system_text:
            try:
                llm_prompt.system_text = llm_prompt.system_text.format(**all_template_inputs.root)
            except KeyError as exc:
                error_msg = f"Could not apply inputs to system_text. KeyError = {exc}. system_text = '{llm_prompt.system_text}'"
                if template_name := self.source_system_template_name:
                    error_msg = f"Error using template named '{template_name}': {error_msg}.\n\n Available inputs: {all_template_inputs.list_keys()}"
                log.error(error_msg)
                raise LLMPromptFactoryError(message=error_msg) from exc
        if llm_prompt.user_text:
            try:
                llm_prompt.user_text = llm_prompt.user_text.format(**all_template_inputs.root)
            except KeyError as exc:
                error_msg = f"Could not apply inputs to user_text. KeyError = {exc}. user_text = '{llm_prompt.user_text}'"
                if template_name := self.source_user_template_name:
                    error_msg = f"Error using template named '{template_name}': {error_msg}.\n\n Available inputs: {all_template_inputs.list_keys()}"
                log.error(error_msg)
                raise LLMPromptFactoryError(message=error_msg) from exc

        return llm_prompt

    @classmethod
    def for_structure_from_preliminary_text(cls) -> "LLMPromptTemplate":
        generic_template_names = get_config().pipelex.generic_template_names
        proto_prompt = LLMPrompt(
            system_text=get_template(generic_template_names.structure_from_preliminary_text_system),
            user_text=get_template(generic_template_names.structure_from_preliminary_text_user),
        )
        return cls(proto_prompt=proto_prompt)
