"""LLM-based code reviewer for quality assessment.

This module provides an alternative to pylint using an LLM as a code reviewer.
The reviewer evaluates code on multiple dimensions and provides a score 0-10.
"""
from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


REVIEWER_SYSTEM_PROMPT = """You are an expert Python code reviewer with 15+ years of experience.
Your task is to evaluate code quality from a software engineering perspective.

You will assess the code on the following dimensions (each 0-10):

1. **Readability** (0-10)
   - Clear variable and function names
   - Appropriate code structure and formatting
   - Self-documenting code vs excessive comments

2. **Maintainability** (0-10)
   - Code organization and modularity
   - Avoidance of code duplication (DRY principle)
   - Ease of future modifications

3. **Correctness** (0-10)
   - Logic correctness and edge case handling
   - Proper error handling
   - Adherence to the task specification

4. **Efficiency** (0-10)
   - Algorithmic efficiency (time complexity)
   - Memory usage
   - Avoidance of unnecessary operations

5. **Pythonic Style** (0-10)
   - Idiomatic Python usage
   - Proper use of built-in functions and data structures
   - Following PEP 8 conventions

Output format (STRICT JSON):
{
    "readability": <0-10>,
    "maintainability": <0-10>,
    "correctness": <0-10>,
    "efficiency": <0-10>,
    "pythonic_style": <0-10>,
    "overall_score": <0-10>,
    "brief_feedback": "<1-2 sentences summarizing main issues>"
}

IMPORTANT:
- Output ONLY valid JSON, no other text
- Be strict but fair - production-quality code should score 7-9
- Excellent code (10) is rare and should be nearly perfect
- Poor code with issues should score 3-5
- Broken/incorrect code should score 0-2
"""


def build_review_prompt(code: str, task_description: str | None = None) -> str:
    """Build the review prompt for the LLM."""
    prompt_parts = ["Please review the following Python code:\n"]
    
    if task_description:
        prompt_parts.append(f"Task Description:\n{task_description}\n")
    
    prompt_parts.append(f"```python\n{code}\n```\n")
    prompt_parts.append("\nProvide your evaluation as JSON with scores 0-10 for each dimension.")
    
    return "\n".join(prompt_parts)


@dataclass
class CodeReviewResult:
    """Result of LLM code review."""
    readability: float
    maintainability: float
    correctness: float
    efficiency: float
    pythonic_style: float
    overall_score: float
    brief_feedback: str
    raw_response: str


def parse_review_response(response: str) -> CodeReviewResult | None:
    """Parse the LLM response into a CodeReviewResult."""
    # Try to extract JSON from the response
    json_match = re.search(r'\{[^{}]*\}', response, re.DOTALL)
    if not json_match:
        return None
    
    try:
        data = json.loads(json_match.group())
        
        return CodeReviewResult(
            readability=float(data.get("readability", 0)),
            maintainability=float(data.get("maintainability", 0)),
            correctness=float(data.get("correctness", 0)),
            efficiency=float(data.get("efficiency", 0)),
            pythonic_style=float(data.get("pythonic_style", 0)),
            overall_score=float(data.get("overall_score", 0)),
            brief_feedback=data.get("brief_feedback", ""),
            raw_response=response,
        )
    except (json.JSONDecodeError, ValueError):
        return None


class CodeReviewer:
    """LLM-based code reviewer."""
    
    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str = "deepseek/deepseek-v3.2",
    ) -> None:
        """Initialize the code reviewer.
        
        Args:
            api_key: OpenAI API key (defaults to REVIEWER_API_KEY env var)
            base_url: API base URL (defaults to OPENAI_BASE_URL env var)
            model: Model to use for review
        """
        self.api_key = api_key or os.environ.get("REVIEWER_API_KEY")
        if not self.api_key:
            raise RuntimeError(
                "REVIEWER_API_KEY environment variable is not set. "
                "Please set it before using the code reviewer."
            )
        
        self.base_url = base_url or os.environ.get("OPENAI_BASE_URL")
        self.model = model
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )
    
    def review_code(
        self,
        code: str,
        task_description: str | None = None,
    ) -> CodeReviewResult | None:
        """Review code and return quality scores.
        
        Args:
            code: Python code to review
            task_description: Optional task context for better evaluation
            
        Returns:
            CodeReviewResult with scores, or None if parsing failed
        """
        prompt = build_review_prompt(code, task_description)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": REVIEWER_SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.1,  # Low temperature for consistent evaluation
                max_tokens=500,
            )
            
            content = response.choices[0].message.content
            if not content:
                return None
            
            return parse_review_response(content)
            
        except Exception as exc:
            print(f"Review error: {exc}")
            return None


def review_code_with_llm(
    code: str,
    task_description: str | None = None,
) -> CodeReviewResult | None:
    """Convenience function to review code using default reviewer.
    
    Args:
        code: Python code to review
        task_description: Optional task context
        
    Returns:
        CodeReviewResult or None
    """
    reviewer = CodeReviewer()
    return reviewer.review_code(code, task_description)
