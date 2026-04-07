from openai import OpenAI

from config import MODEL_CONFIG
from prompts import SYSTEM_RULES


class LLMClient:
    def __init__(self) -> None:
        self.client = OpenAI(
            api_key="sk-mTk0RYw5fkeWo1Y8k_bc1nWMQueTpE86",
            base_url="https://routerai.ru/api/v1"
        )

    def generate_code(self, user_prompt: str) -> str:
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
                    "WinError 2 при HTTP-запросе к API: «файл не найден». "
                    "Проверьте SSL (certifi), переменные SSL_CERT_FILE/REQUESTS_CA_BUNDLE, "
                    "прокси и доступность base_url. "
                    f"Исходная ошибка: {exc}"
                ) from exc
            raise

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("Модель вернула пустой ответ")

        return content.strip()