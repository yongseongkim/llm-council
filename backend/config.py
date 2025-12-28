"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv
from llm_router import LLMRouter

load_dotenv()

# Council members - provider/model format
COUNCIL_MODELS = [
    "openai/gpt-5.2",
    "anthropic/claude-opus-4-5-20251101",
    "google/gemini-3.0-pro",
    "xai/grok-4",
    "zai/glm-4.6",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemini-3.0-pro"

# Model for generating conversation titles
TITLE_GENERATION_MODEL = "google/gemini-2.0-flash"

# Data directory for conversation storage
DATA_DIR = "data/conversations"


def create_router() -> LLMRouter:
    """Create and configure the LLM router."""
    router = LLMRouter()

    # Configure providers from environment variables
    if os.getenv("OPENAI_API_KEY"):
        router.configure("openai", api_key=os.getenv("OPENAI_API_KEY"))

    if os.getenv("ANTHROPIC_API_KEY"):
        router.configure("anthropic", api_key=os.getenv("ANTHROPIC_API_KEY"))

    if os.getenv("GOOGLE_API_KEY"):
        router.configure("google", api_key=os.getenv("GOOGLE_API_KEY"))

    if os.getenv("XAI_API_KEY"):
        router.configure("xai", api_key=os.getenv("XAI_API_KEY"))

    if os.getenv("ZAI_API_KEY"):
        router.configure("zai", api_key=os.getenv("ZAI_API_KEY"))

    if os.getenv("DEEPSEEK_API_KEY"):
        router.configure("deepseek", api_key=os.getenv("DEEPSEEK_API_KEY"))

    return router


# Global router instance
router = create_router()
