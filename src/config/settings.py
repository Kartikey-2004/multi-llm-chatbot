from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    # API KEYS

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    # ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    OPENAI_MODEL = "gpt-4o-mini"
    GEMINI_MODEL = "gemini-2.5-flash"
    # CLAUDE_MODEL = "claude-sonnet-4-20250514"

    TEMPERATURE = 0.2
    MAX_RETRIES = 2
    DEBUG = True


settings = Settings()
