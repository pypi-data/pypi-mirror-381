from typing import Any

from pydantic import BaseModel, Field

from pipelex.tools.templating.jinja2_template_category import Jinja2TemplateCategory
from pipelex.tools.templating.templating_models import PromptingStyle


class Jinja2Blueprint(BaseModel):
    jinja2_name: str | None = Field(default=None, description="Name of the Jinja2 template to use")
    jinja2: str | None = Field(default=None, description="Raw Jinja2 template string")
    prompting_style: PromptingStyle | None = Field(default=None, description="Style of prompting to use (typically for different LLMs)")
    template_category: Jinja2TemplateCategory = Field(
        default=Jinja2TemplateCategory.LLM_PROMPT,
        description="Category of the template (could also be HTML, MARKDOWN, MERMAID, etc.), influences Jinja2 rendering environment config",
    )
    extra_context: dict[str, Any] | None = Field(default=None, description="Additional context variables for template rendering")
