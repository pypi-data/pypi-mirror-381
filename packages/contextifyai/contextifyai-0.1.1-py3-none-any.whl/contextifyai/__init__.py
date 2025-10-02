"""
ContextifyAI - Drop-in replacement for Vercel AI SDK with automatic tracking

Just change your import from:
    from ai_sdk import generate_text, anthropic
To:
    from contextifyai import generate_text, anthropic

Everything else stays the same!
"""

from .config import configure

# Drop-in replacements for Vercel AI SDK
from .vercel_compatible import generate_text, anthropic, openai

__version__ = "0.1.1"
__all__ = [
    "configure",
    # Vercel AI SDK compatible (drop-in replacement)
    "generate_text",
    "anthropic",
    "openai",
]
