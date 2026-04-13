"""LLM Client wrapper for OpenAI API."""

import os
from openai import OpenAI

from config import MODEL_CONFIG
from prompts import SYSTEM_RULES


def _get_api_key() -> str:
    """Get API key from environment variable."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY environment variable is not set. "
            "Please set it before running the pipeline:\n"
            "  export OPENAI_API_KEY=your_key_here  # Linux/macOS\n"
            "  set OPENAI_API_KEY=your_key_here      # Windows CMD\n"
            "  $env:OPENAI_API_KEY='your_key_here'   # Windows PowerShell\n"
            "Or create a .env file based on .env.example"
        )
    return api_key


def _get_base_url() -> str | None:
    """Get optional base URL from environment variable."""
    return os.environ.get("OPENAI_BASE_URL")


class LLMClient:
    """Client for generating code using OpenAI-compatible API."""

    def __init__(self) -> None:
        self.client = OpenAI(
            api_key=_get_api_key(),
            base_url=_get_base_url()
        )

    def generate_code(self, user_prompt: str) -> str:
        """Generate code using the LLM.
        
        Args:
            user_prompt: The prompt describing the coding task.
            
        Returns:
            Generated code as string.
            
        Raises:
            RuntimeError: If the model returns an empty response.
        """
        try:
            response = self.client.chat.completions.create(
                model=MODEL_CONFIG.model_name,
                messages=[
                    {"role": "system", "content": SYSTEM_RULES},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=MODEL_CONFIG.temperature,
                max_tokens=MODEL_CONFIG.max_output_tokens,
            )
        except OSError as exc:
            errno = getattr(exc, "errno", None)
            winerr = getattr(exc, "winerror", None)
            if errno == 2 or winerr == 2:
                raise RuntimeError(
                    "WinError 2 during HTTP request to API: 'file not found'. "
                    "Check SSL (certifi), SSL_CERT_FILE/REQUESTS_CA_BUNDLE variables, "
                    "proxy and base_url availability. "
                    f"Original error: {exc}"
                ) from exc
            raise

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("Model returned empty response")

        return content.strip()
