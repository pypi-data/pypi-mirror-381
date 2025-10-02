"""
Configuration management for ContextifyAI
"""
import os
from typing import Optional

class Config:
    """Global configuration for ContextifyAI"""

    def __init__(self):
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.promptflow_url = os.getenv("PROMPTFLOW_URL", "http://localhost:8000")
        self.promptflow_api_key = os.getenv("PROMPTFLOW_API_KEY", "pk_test_123456")
        self.default_model = "claude-3-5-sonnet-20241022"
        self.default_temperature = 0.7
        self.default_max_tokens = 1000

    def update(
        self,
        anthropic_api_key: Optional[str] = None,
        openai_api_key: Optional[str] = None,
        promptflow_url: Optional[str] = None,
        promptflow_api_key: Optional[str] = None,
        default_model: Optional[str] = None,
        default_temperature: Optional[float] = None,
        default_max_tokens: Optional[int] = None
    ):
        """Update configuration"""
        if anthropic_api_key:
            self.anthropic_api_key = anthropic_api_key
        if openai_api_key:
            self.openai_api_key = openai_api_key
        if promptflow_url:
            self.promptflow_url = promptflow_url
        if promptflow_api_key:
            self.promptflow_api_key = promptflow_api_key
        if default_model:
            self.default_model = default_model
        if default_temperature is not None:
            self.default_temperature = default_temperature
        if default_max_tokens:
            self.default_max_tokens = default_max_tokens

# Global config instance
_config = Config()

def configure(**kwargs):
    """
    Configure ContextifyAI globally.

    Args:
        anthropic_api_key: Anthropic API key
        openai_api_key: OpenAI API key
        promptflow_url: PromptFlow backend URL
        promptflow_api_key: PromptFlow API key
        default_model: Default model to use
        default_temperature: Default temperature
        default_max_tokens: Default max tokens

    Example:
        >>> from contextifyai import configure
        >>> configure(
        ...     anthropic_api_key="sk-ant-...",
        ...     promptflow_url="http://localhost:8000"
        ... )
    """
    _config.update(**kwargs)

def get_config() -> Config:
    """Get global configuration"""
    return _config
