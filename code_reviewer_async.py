"""Async LLM-based code reviewer for quality assessment.

This module provides an async version of the code reviewer that can be used
for parallel code quality evaluation.
"""
from __future__ import annotations

import asyncio
import json
import os
import re
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

from code_reviewer import (
    REVIEWER_SYSTEM_PROMPT,
    build_review_prompt,
    CodeReviewResult,
    parse_review_response,
)


def _get_reviewer_api_key() -> str:
    """Get reviewer API key from environment variable."""
    api_key = os.environ.get("REVIEWER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "REVIEWER_API_KEY environment variable is not set. "
            "Please set it before using the async code reviewer."
        )
    return api_key


def _get_reviewer_base_url() -> str:
    """Get optional base URL from environment variable."""
    base_url = os.environ.get("OPENAI_BASE_URL")
    return base_url if base_url else "https://api.openai.com/v1"


@dataclass
class ReviewRequest:
    """Represents a single code review request."""
    task_id: str
    strategy: str
    sample_index: int
    code: str
    task_description: str | None = None


@dataclass
class ReviewResult:
    """Result of a code review request."""
    task_id: str
    strategy: str
    sample_index: int
    review: CodeReviewResult | None
    error: str | None = None


class AsyncCodeReviewer:
    """Async LLM-based code reviewer with concurrent request support.
    
    Uses the same API as CodeReviewer but with async/await support.
    """
    
    def __init__(
        self,
        model: str = "deepseek/deepseek-v3.2",
        max_concurrent: int = 10,
        max_retries: int = 3,
        timeout_seconds: float = 60.0,
    ) -> None:
        """Initialize the async code reviewer.
        
        Args:
            model: Model to use for review.
            max_concurrent: Maximum concurrent review requests.
            max_retries: Maximum retries for failed requests.
            timeout_seconds: Timeout for each review request.
        """
        self.api_key = _get_reviewer_api_key()
        self.base_url = _get_reviewer_base_url().rstrip("/")
        self.model = model
        self.max_concurrent = max_concurrent
        self.max_retries = max_retries
        self.timeout_seconds = timeout_seconds
        self._session: aiohttp.ClientSession | None = None
        self._semaphore: asyncio.Semaphore | None = None
    
    async def __aenter__(self) -> "AsyncCodeReviewer":
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
    
    async def review_code(
        self,
        code: str,
        task_description: str | None = None,
    ) -> CodeReviewResult | None:
        """Review code asynchronously.
        
        Args:
            code: Python code to review.
            task_description: Optional task context for better evaluation.
            
        Returns:
            CodeReviewResult with scores, or None if parsing failed.
        """
        if not self._session:
            raise RuntimeError("AsyncCodeReviewer must be used as async context manager")
        
        async with self._semaphore:
            return await self._review_with_retry(code, task_description)
    
    async def _review_with_retry(
        self,
        code: str,
        task_description: str | None = None,
    ) -> CodeReviewResult | None:
        """Review code with exponential backoff retry."""
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
                    return await self._review_single(code, task_description)
        except RetryError:
            return None
        except Exception as e:
            print(f"Review error: {e}")
            return None
    
    async def _review_single(
        self,
        code: str,
        task_description: str | None = None,
    ) -> CodeReviewResult | None:
        """Make a single review API request."""
        prompt = build_review_prompt(code, task_description)
        url = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": REVIEWER_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.1,  # Low temperature for consistent evaluation
            "max_tokens": 500,
        }
        
        async with self._session.post(url, json=payload) as response:
            if response.status == 429:
                retry_after = float(response.headers.get("Retry-After", "5"))
                await asyncio.sleep(retry_after)
                raise aiohttp.ClientError("Rate limited")
            
            response.raise_for_status()
            data = await response.json()
        
        content = data.get("choices", [{}])[0].get("message", {}).get("content")
        if not content:
            return None
        
        return parse_review_response(content)
    
    async def review_batch(
        self,
        requests: list[ReviewRequest],
        progress_callback: Any = None,
    ) -> list[ReviewResult]:
        """Review multiple code samples concurrently.
        
        Args:
            requests: List of review requests.
            progress_callback: Optional async callback for progress updates.
            
        Returns:
            List of review results in the same order as requests.
        """
        if not self._session:
            raise RuntimeError("AsyncCodeReviewer must be used as async context manager")
        
        results: list[ReviewResult] = [None] * len(requests)  # type: ignore
        completed = 0
        total = len(requests)
        
        async def process_request(index: int, request: ReviewRequest) -> None:
            nonlocal completed
            try:
                review = await self.review_code(request.code, request.task_description)
                results[index] = ReviewResult(
                    task_id=request.task_id,
                    strategy=request.strategy,
                    sample_index=request.sample_index,
                    review=review,
                )
            except Exception as e:
                results[index] = ReviewResult(
                    task_id=request.task_id,
                    strategy=request.strategy,
                    sample_index=request.sample_index,
                    review=None,
                    error=str(e),
                )
            finally:
                completed += 1
                if progress_callback:
                    await progress_callback(completed, total, request)
        
        tasks = [
            process_request(i, req)
            for i, req in enumerate(requests)
        ]
        await asyncio.gather(*tasks)
        
        return results


async def review_codes_concurrent(
    codes: list[tuple[str, str | None]],  # (code, task_description) pairs
    max_concurrent: int = 10,
) -> list[CodeReviewResult | None]:
    """Convenience function to review multiple codes concurrently.
    
    Args:
        codes: List of (code, task_description) tuples.
        max_concurrent: Maximum concurrent requests.
        
    Returns:
        List of review results in the same order as input.
    """
    async with AsyncCodeReviewer(max_concurrent=max_concurrent) as reviewer:
        tasks = [
            reviewer.review_code(code, task_desc)
            for code, task_desc in codes
        ]
        return await asyncio.gather(*tasks)
