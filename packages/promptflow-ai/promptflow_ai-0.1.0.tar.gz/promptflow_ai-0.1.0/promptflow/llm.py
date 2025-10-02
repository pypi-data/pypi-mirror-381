"""
PromptFlowLLM - Drop-in replacement for OpenAI/Anthropic clients with automatic tracking.

Usage:
    from promptflow import PromptFlowLLM

    # Initialize once
    llm = PromptFlowLLM(provider="openai", model="gpt-4")

    # Use in your agent - specify prompt_name per call
    response = llm.chat.completions.create(
        prompt_name="analyze-query",
        messages=[{"role": "user", "content": "..."}]
    )
"""

import os
import time
import uuid
from typing import Optional, List, Dict, Any, Union
import requests


class PromptFlowLLM:
    """
    Drop-in replacement for OpenAI/Anthropic clients with automatic tracking.

    Features:
    - Wraps LLM provider clients (OpenAI, Anthropic, etc.)
    - Automatically tracks every LLM call
    - Fetches versioned prompts from PromptFlow backend
    - Tracks latency, tokens, cost per call
    - Instance and session tracking for multi-user scenarios
    """

    def __init__(
        self,
        provider: str = "openai",
        model: str = "gpt-4",
        promptflow_api_key: Optional[str] = None,
        promptflow_url: str = "https://backend-black-six-59.vercel.app",
        instance_id: Optional[str] = None,
        auto_generate_session_id: bool = True,
        **provider_kwargs
    ):
        """
        Initialize PromptFlowLLM wrapper.

        Args:
            provider: LLM provider ("openai", "anthropic", "custom")
            model: Model name (e.g., "gpt-4", "claude-3-opus")
            promptflow_api_key: PromptFlow API key (or set PROMPTFLOW_API_KEY env var)
            promptflow_url: PromptFlow backend URL
            instance_id: Optional instance ID for tracking (auto-generated if not provided)
            auto_generate_session_id: Auto-generate session ID per call (default True)
            **provider_kwargs: Additional kwargs for the provider client
        """
        self.provider = provider
        self.model = model
        self.promptflow_url = promptflow_url
        self.promptflow_api_key = promptflow_api_key or os.getenv("PROMPTFLOW_API_KEY")
        self.instance_id = instance_id or f"instance_{uuid.uuid4().hex[:8]}"
        self.auto_generate_session_id = auto_generate_session_id

        if not self.promptflow_api_key:
            raise ValueError(
                "PromptFlow API key required. Set PROMPTFLOW_API_KEY env var or pass promptflow_api_key parameter."
            )

        # Initialize provider client
        if provider == "openai":
            from openai import OpenAI
            self._client = OpenAI(**provider_kwargs)
        elif provider == "anthropic":
            from anthropic import Anthropic
            self._client = Anthropic(**provider_kwargs)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

        # Create chat.completions wrapper (nested structure)
        self.chat = Chat(self)

    def _track_call(
        self,
        prompt_name: str,
        input_messages: List[Dict[str, str]],
        output_message: str,
        latency_ms: int,
        input_tokens: Optional[int] = None,
        output_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        cost: Optional[float] = None,
        session_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Send tracking data to PromptFlow backend."""
        try:
            response = requests.post(
                f"{self.promptflow_url}/llm/track",
                headers={"X-API-Key": self.promptflow_api_key},
                json={
                    "prompt_name": prompt_name,
                    "model": self.model,
                    "provider": self.provider,
                    "input_messages": input_messages,
                    "output_message": output_message,
                    "latency_ms": latency_ms,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                    "total_tokens": total_tokens,
                    "cost": cost,
                    "instance_id": self.instance_id,
                    "session_id": session_id,
                    "metadata": metadata or {}
                }
            )
            response.raise_for_status()
        except Exception as e:
            # Don't fail the LLM call if tracking fails
            print(f"Warning: Failed to track LLM call: {e}")

    def _calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost based on model pricing."""
        # Pricing per 1M tokens (as of 2024)
        pricing = {
            "gpt-4": {"input": 30.0, "output": 60.0},
            "gpt-4-turbo": {"input": 10.0, "output": 30.0},
            "gpt-3.5-turbo": {"input": 0.5, "output": 1.5},
            "claude-3-opus": {"input": 15.0, "output": 75.0},
            "claude-3-sonnet": {"input": 3.0, "output": 15.0},
        }

        if self.model not in pricing:
            return 0.0

        input_cost = (input_tokens / 1_000_000) * pricing[self.model]["input"]
        output_cost = (output_tokens / 1_000_000) * pricing[self.model]["output"]

        return round(input_cost + output_cost, 6)


class Chat:
    """Wrapper for chat namespace."""

    def __init__(self, parent: PromptFlowLLM):
        self.completions = ChatCompletions(parent)


class ChatCompletions:
    """Wrapper for chat.completions API."""

    def __init__(self, parent: PromptFlowLLM):
        self.parent = parent

    def create(
        self,
        prompt_name: Optional[str] = None,
        messages: Optional[List[Dict[str, str]]] = None,
        session_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Create a chat completion with automatic tracking.

        Args:
            prompt_name: Name of the prompt in PromptFlow (optional)
            messages: Chat messages (if not using versioned prompt)
            session_id: Optional session ID for grouping calls
            metadata: Optional metadata to attach to this call
            **kwargs: Additional arguments to pass to the provider
        """
        # Generate session ID if auto-generation is enabled
        if session_id is None and self.parent.auto_generate_session_id:
            session_id = f"session_{uuid.uuid4().hex[:8]}"

        # Track start time
        start_time = time.time()

        # Call the actual LLM
        if self.parent.provider == "openai":
            response = self.parent._client.chat.completions.create(
                model=self.parent.model,
                messages=messages,
                **kwargs
            )

            # Extract response data
            output_message = response.choices[0].message.content
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens

        elif self.parent.provider == "anthropic":
            # Convert OpenAI format to Anthropic format
            system_messages = [m["content"] for m in messages if m["role"] == "system"]
            user_messages = [m for m in messages if m["role"] != "system"]

            response = self.parent._client.messages.create(
                model=self.parent.model,
                system=system_messages[0] if system_messages else "",
                messages=user_messages,
                **kwargs
            )

            output_message = response.content[0].text
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            total_tokens = input_tokens + output_tokens

        else:
            raise ValueError(f"Unsupported provider: {self.parent.provider}")

        # Calculate latency
        latency_ms = int((time.time() - start_time) * 1000)

        # Calculate cost
        cost = self.parent._calculate_cost(input_tokens, output_tokens)

        # Track the call (only if prompt_name is provided)
        if prompt_name:
            self.parent._track_call(
                prompt_name=prompt_name,
                input_messages=messages,
                output_message=output_message,
                latency_ms=latency_ms,
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                total_tokens=total_tokens,
                cost=cost,
                session_id=session_id,
                metadata=metadata
            )

        return response
