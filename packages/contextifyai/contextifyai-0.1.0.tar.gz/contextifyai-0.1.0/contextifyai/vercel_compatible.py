"""
Vercel AI SDK compatible API with automatic tracking.

This module provides drop-in replacements for ai_sdk functions.
Just change your import and everything gets tracked automatically!
"""
import time
import uuid
import requests
from typing import Optional
from ai_sdk import generate_text as _original_generate_text
from ai_sdk import anthropic as _original_anthropic
from ai_sdk import openai as _original_openai

from .config import get_config


def _track_to_promptflow(
    prompt: str,
    response_text: str,
    model_name: str,
    provider: str,
    latency_ms: int,
    prompt_name: Optional[str] = None,
    session_id: Optional[str] = None,
    metadata: Optional[dict] = None
):
    """Track the call to PromptFlow backend"""
    config = get_config()

    try:
        requests.post(
            f"{config.promptflow_url}/llm/track",
            headers={"X-API-Key": config.promptflow_api_key},
            json={
                "prompt_name": prompt_name or f"prompt_{uuid.uuid4().hex[:8]}",
                "model": model_name,
                "provider": provider,
                "input_messages": [{"role": "user", "content": prompt}],
                "output_message": response_text,
                "latency_ms": latency_ms,
                "session_id": session_id or f"session_{uuid.uuid4().hex[:8]}",
                "metadata": metadata or {},
                "instance_id": "contextifyai"
            },
            timeout=5
        )
    except Exception as e:
        # Silently fail if tracking fails - don't break user's code
        pass


def generate_text(model, prompt: Optional[str] = None, prompt_template: Optional[str] = None, **kwargs):
    """
    Drop-in replacement for ai_sdk.generate_text() with automatic tracking.

    Usage:
        # Before (Vercel AI SDK):
        from ai_sdk import generate_text, anthropic
        model = anthropic("claude-3-5-sonnet-20241022", api_key=key)
        result = generate_text(model=model, prompt="Hello")

        # After (ContextifyAI - same code works):
        from contextifyai import generate_text, anthropic
        model = anthropic("claude-3-5-sonnet-20241022", api_key=key)
        result = generate_text(model=model, prompt="Hello")
        # Now everything is tracked automatically!

        # NEW: Template-based prompts (editable from dashboard):
        result = generate_text(model=model, prompt_template="greeting")
        # Fetches latest template from backend - editable without code changes!

    Args:
        model: Model instance from anthropic() or openai()
        prompt: The prompt text (original Vercel AI SDK way)
        prompt_template: Template name to fetch from backend (NEW - editable from dashboard)
        **kwargs: All other arguments (system, temperature, max_tokens, etc.)

    Returns:
        Same result object as ai_sdk.generate_text()
    """
    # NEW: Fetch template from backend if prompt_template is provided
    template_name = None
    if prompt_template:
        config = get_config()
        try:
            response = requests.get(
                f"{config.promptflow_url}/prompts/templates/{prompt_template}",
                headers={"X-API-Key": config.promptflow_api_key},
                timeout=5
            )
            if response.ok:
                template_data = response.json()
                prompt = template_data['template']
                template_name = prompt_template

                # Substitute variables if provided
                variables = kwargs.pop('variables', None)
                if variables and template_data.get('variables'):
                    prompt = prompt.format(**variables)
            else:
                raise ValueError(f"Template '{prompt_template}' not found in backend")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to fetch template '{prompt_template}': {str(e)}")

    # Ensure we have a prompt
    if not prompt:
        raise ValueError("Either 'prompt' or 'prompt_template' must be provided")

    # Track start time
    start_time = time.time()

    # Call original generate_text
    result = _original_generate_text(model=model, prompt=prompt, **kwargs)

    # Calculate latency
    latency_ms = int((time.time() - start_time) * 1000)

    # Extract model info
    model_name = getattr(model, 'model_id', 'unknown')
    provider = getattr(model, 'provider_id', 'unknown')

    # Track to PromptFlow (use template name if available)
    _track_to_promptflow(
        prompt=prompt,
        response_text=result.text,
        model_name=model_name,
        provider=provider,
        latency_ms=latency_ms,
        prompt_name=template_name  # Track with template name for better organization
    )

    return result


def anthropic(model_id: str, api_key: Optional[str] = None, **kwargs):
    """
    Drop-in replacement for ai_sdk.anthropic() with automatic model info tracking.

    Usage:
        # Before:
        from ai_sdk import anthropic
        model = anthropic("claude-3-5-sonnet-20241022", api_key=key)

        # After (just change import):
        from contextifyai import anthropic
        model = anthropic("claude-3-5-sonnet-20241022", api_key=key)

    Args:
        model_id: Claude model ID
        api_key: Anthropic API key (optional if set in config)
        **kwargs: Other arguments

    Returns:
        Same model instance as ai_sdk.anthropic()
    """
    config = get_config()

    # Use provided api_key or fall back to config
    final_api_key = api_key or config.anthropic_api_key

    if not final_api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY not set. Either:\n"
            "  1. Pass api_key parameter: anthropic('model', api_key='...')\n"
            "  2. Set environment variable: ANTHROPIC_API_KEY=...\n"
            "  3. Call configure(anthropic_api_key='...')"
        )

    # Call original anthropic function
    return _original_anthropic(model_id, api_key=final_api_key, **kwargs)


def openai(model_id: str, api_key: Optional[str] = None, **kwargs):
    """
    Drop-in replacement for ai_sdk.openai() with automatic model info tracking.

    Usage:
        # Before:
        from ai_sdk import openai
        model = openai("gpt-4", api_key=key)

        # After (just change import):
        from contextifyai import openai
        model = openai("gpt-4", api_key=key)

    Args:
        model_id: OpenAI model ID
        api_key: OpenAI API key (optional if set in config)
        **kwargs: Other arguments

    Returns:
        Same model instance as ai_sdk.openai()
    """
    config = get_config()

    # Use provided api_key or fall back to config
    final_api_key = api_key or config.openai_api_key

    if not final_api_key:
        raise ValueError(
            "OPENAI_API_KEY not set. Either:\n"
            "  1. Pass api_key parameter: openai('model', api_key='...')\n"
            "  2. Set environment variable: OPENAI_API_KEY=...\n"
            "  3. Call configure(openai_api_key='...')"
        )

    # Call original openai function
    return _original_openai(model_id, api_key=final_api_key, **kwargs)
