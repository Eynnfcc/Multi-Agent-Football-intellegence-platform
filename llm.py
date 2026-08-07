from crewai import LLM

from config import (
    GEMINI_API_KEY,
    LLM_MODEL,
    LLM_TEMPERATURE,
)


if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Add it to your .env file."
    )


llm = LLM(
    model=LLM_MODEL,
    api_key=GEMINI_API_KEY,
    temperature=LLM_TEMPERATURE,
)