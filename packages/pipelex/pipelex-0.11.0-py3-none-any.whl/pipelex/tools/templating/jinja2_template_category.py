from collections.abc import Callable
from typing import Any

from jinja2.runtime import Context

from pipelex.tools.templating.jinja2_filters import tag, text_format
from pipelex.tools.templating.jinja2_models import Jinja2FilterName
from pipelex.tools.templating.templating_models import TextFormat
from pipelex.types import StrEnum


# TODO: add more categories
class Jinja2TemplateCategory(StrEnum):
    HTML = "html"
    MARKDOWN = "markdown"
    MERMAID = "mermaid"
    LLM_PROMPT = "llm_prompt"

    @property
    def filters(self) -> dict[Jinja2FilterName, Callable[[Context, Any, TextFormat | None], Any]]:
        match self:
            case Jinja2TemplateCategory.MERMAID:
                return {}
            case Jinja2TemplateCategory.HTML | Jinja2TemplateCategory.MARKDOWN:
                return {
                    Jinja2FilterName.FORMAT: text_format,
                    Jinja2FilterName.TAG: tag,
                }
            case Jinja2TemplateCategory.LLM_PROMPT:
                return {
                    Jinja2FilterName.FORMAT: text_format,
                    Jinja2FilterName.TAG: tag,
                }
