"""Async LLM Client wrapper for OpenAI API with concurrent request support."""

from __future__ import annotations

import asyncio
import os
from dataclasses import dataclass
from typing import Any

import aiohttp
from tenacity import (
    AsyncRetrying,
    RetryError,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

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


def _get_base_url() -> str:
    """Get optional base URL from environment variable, defaults to OpenAI."""
    base_url = os.environ.get("OPENAI_BASE_URL")
    return base_url if base_url else "https://api.openai.com/v1"


@dataclass
class GenerationRequest:
    """Represents a single code generation request."""
    task_id: str
    strategy: str
    sample_index: int
    prompt: str
    # For self_refine strategy
    is_refinement: bool = False
    previous_code: str | None = None
    feedback: str | None = None


@dataclass
class GenerationResult:
    """Result of a code generation request."""
    task_id: str
    strategy: str
    sample_index: int
    code: str
    is_refinement: bool = False
    error: str | None = None
    latency_ms: float = 0.0


class AsyncLLMClient:
    """Async client for generating code using OpenAI-compatible API.
    
    Supports concurrent requests with rate limiting and retry logic.
    """

    def __init__(
        self,
        model: str | None = None,
        temperature: float | None = None,
        max_output_tokens: int | None = None,
        max_concurrent: int = 10,
        max_retries: int = 3,
        timeout_seconds: float = 120.0,
    ) -> None:
        """Initialize the async LLM client.
        
        Args:
            model: Модель-генератор. Если None — берётся из MODEL_CONFIG.model_name.
            temperature: Температура. Если None — берётся из MODEL_CONFIG.
            max_output_tokens: Лимит токенов. Если None — из MODEL_CONFIG.
            max_concurrent: Maximum number of concurrent API requests.
            max_retries: Maximum number of retries for failed requests.
            timeout_seconds: Timeout for each API request.
        """
        self.api_key = _get_api_key()
        self.base_url = _get_base_url().rstrip("/")
        self.model = model or MODEL_CONFIG.model_name
        self.temperature = temperature if temperature is not None else MODEL_CONFIG.temperature
        self.max_output_tokens = max_output_tokens if max_output_tokens is not None else MODEL_CONFIG.max_output_tokens
        self.max_concurrent = max_concurrent
        self.max_retries = max_retries
        self.timeout_seconds = timeout_seconds
        self._session: aiohttp.ClientSession | None = None
        self._semaphore: asyncio.Semaphore | None = None

    async def __aenter__(self) -> "AsyncLLMClient":
        """Create aiohttp session on context manager entry."""
        self._session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout_seconds),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
        )
        self._semaphore = asyncio.Semaphore(self.max_concurrent)
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Close aiohttp session on context manager exit."""
        if self._session:
            await self._session.close()
            self._session = None

    async def generate_code(self, user_prompt: str) -> str:
        """Generate code using the LLM (async version).
        
        Args:
            user_prompt: The prompt describing the coding task.
            
        Returns:
            Generated code as string.
            
        Raises:
            RuntimeError: If the model returns an empty response or all retries fail.
        """
        if not self._session:
            raise RuntimeError("AsyncLLMClient must be used as async context manager")

        async with self._semaphore:
            return await self._generate_with_retry(user_prompt)

    async def _generate_with_retry(self, user_prompt: str) -> str:
        """Generate code with exponential backoff retry."""
        try:
            async for attempt in AsyncRetrying(
                stop=stop_after_attempt(self.max_retries),
                wait=wait_exponential(multiplier=1, min=2, max=30),
                retry=retry_if_exception_type(
                    (aiohttp.ClientError, asyncio.TimeoutError)
                ),
                reraise=True,
            ):
                with attempt:
                    return await self._generate_single(user_prompt)
        except RetryError as e:
            raise RuntimeError(f"All {self.max_retries} retries failed") from e

    async def _generate_single(self, user_prompt: str) -> str:
        """Make a single API request."""
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SYSTEM_RULES},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self.temperature,
            "max_tokens": self.max_output_tokens,
        }

        async with self._session.post(url, json=payload) as response:
            if response.status == 429:
                # Rate limited - wait and retry
                retry_after = float(response.headers.get("Retry-After", "5"))
                await asyncio.sleep(retry_after)
                raise aiohttp.ClientError("Rate limited")
            
            response.raise_for_status()
            data = await response.json()

        content = data.get("choices", [{}])[0].get("message", {}).get("content")
        if not content:
            raise RuntimeError("Model returned empty response")

        return content.strip()

    async def generate_batch(
        self,
        requests: list[GenerationRequest],
        progress_callback: Any = None,
    ) -> list[GenerationResult]:
        """Generate code for multiple requests concurrently.
        
        Args:
            requests: List of generation requests.
            progress_callback: Optional async callback for progress updates.
            
        Returns:
            List of generation results in the same order as requests.
        """
        if not self._session:
            raise RuntimeError("AsyncLLMClient must be used as async context manager")

        results: list[GenerationResult] = [None] * len(requests)  # type: ignore
        completed = 0
        total = len(requests)

        async def process_request(index: int, request: GenerationRequest) -> None:
            nonlocal completed
            try:
                code = await self.generate_code(request.prompt)
                results[index] = GenerationResult(
                    task_id=request.task_id,
                    strategy=request.strategy,
                    sample_index=request.sample_index,
                    code=code,
                    is_refinement=request.is_refinement,
                )
            except Exception as e:
                results[index] = GenerationResult(
                    task_id=request.task_id,
                    strategy=request.strategy,
                    sample_index=request.sample_index,
                    code="",
                    error=str(e),
                    is_refinement=request.is_refinement,
                )
            finally:
                completed += 1
                if progress_callback:
                    await progress_callback(completed, total, request)

        # Run all requests concurrently (limited by semaphore)
        tasks = [
            process_request(i, req) 
            for i, req in enumerate(requests)
        ]
        await asyncio.gather(*tasks)

        return results


async def generate_codes_concurrent(
    prompts: list[str],
    max_concurrent: int = 10,
) -> list[str]:
    """Convenience function to generate multiple codes concurrently.
    
    Args:
        prompts: List of prompts to generate code for.
        max_concurrent: Maximum concurrent requests.
        
    Returns:
        List of generated codes in the same order as prompts.
    """
    async with AsyncLLMClient(max_concurrent=max_concurrent) as client:
        tasks = [client.generate_code(prompt) for prompt in prompts]
        return await asyncio.gather(*tasks)
