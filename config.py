from pathlib import Path
import os

from dotenv import load_dotenv


# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)


# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv(BASE_DIR / ".env")


# ==========================================================
# API Keys
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SGAI_API_KEY = os.getenv("SGAI_API_KEY")


# ==========================================================
# AI Configuration
# ==========================================================

LLM_MODEL = "gemini/gemini-3.5-flash-lite"
LLM_TEMPERATURE = 0.7


# ==========================================================
# Search Configuration
# ==========================================================

MAX_SEARCH_RESULTS = 10
SEARCH_DEPTH = "advanced"
SEARCH_TOPIC = "general"


# ==========================================================
# Scraping Configuration
# ==========================================================

MAX_PAGES_TO_SCRAPE = 10
SCRAPING_TIMEOUT_SECONDS = 60


# ==========================================================
# CrewAI Configuration
# ==========================================================

CREW_VERBOSE = True
AGENT_MAX_ITERATIONS = 3


# ==========================================================
# Club Information
# ==========================================================

CLUB_NAME = "European Football Club"

CLUB_DESCRIPTION = (
    "A professional European football club searching for "
    "high-quality players using data-driven recruitment."
)

CLUB_PLAYING_STYLE = (
    "High pressing, quick transitions, technical quality, "
    "and intelligent positional play."
)

DEFAULT_CURRENCY = "EUR"


# ==========================================================
# Report
# ==========================================================

REPORT_TITLE = "AI Football Scouting Report"


# ---------------------------------------------------------
# 10. Configuration validation
# ---------------------------------------------------------

def validate_config() -> None:
    """
    Validate that all required settings are available before the
    multi-agent system starts.

    Raises:
        RuntimeError: If a required environment variable is missing
        or if ranking weights do not add up to 1.0.
    """

    missing_variables = []

    if not GEMINI_API_KEY:
        missing_variables.append("GEMINI_API_KEY")

    if not TAVILY_API_KEY:
        missing_variables.append("TAVILY_API_KEY")

    if not SGAI_API_KEY:
        missing_variables.append("SGAI_API_KEY")

    if missing_variables:
        missing_text = ", ".join(missing_variables)

        raise RuntimeError(
            "Missing required environment variables: "
            f"{missing_text}. Add them to the .env file."
        )
