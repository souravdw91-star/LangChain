import os
from pathlib import Path
from dotenv import load_dotenv


def _find_env_file():
    """Locate the workspace root .env file by walking up from this module."""
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        env_path = parent / ".env"
        if env_path.exists():
            return env_path
    return current.parents[1] / ".env"


def configure_langsmith():
    """Load LangSmith settings from the environment and apply them to os.environ."""
    load_dotenv(dotenv_path=_find_env_file())

    langsmith_api_key = (
        os.getenv("LANGCHAIN_API_KEY")
        or os.getenv("LANGSMITH_API_KEY")
        or os.getenv("LangChain_ChatBot_API_KEY")
    )

    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "Learning")
    os.environ.setdefault("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")

    if langsmith_api_key:
        os.environ["LANGCHAIN_API_KEY"] = langsmith_api_key
        os.environ["LANGSMITH_API_KEY"] = langsmith_api_key
        os.environ["LANGCHAIN_TRACING_V2"] = "true"

        try:
            from langsmith import Client

            # list_projects returns an Iterator; evaluate the first item to trigger the request.
            next(Client(api_key=langsmith_api_key).list_projects(), None)
            tracing_enabled = True
            validation_error = None
        except Exception as exc:  # noqa: BLE001
            tracing_enabled = False
            validation_error = str(exc)
            os.environ["LANGCHAIN_TRACING_V2"] = "false"
    else:
        tracing_enabled = False
        validation_error = "No LangSmith API key found in environment."
        os.environ["LANGCHAIN_TRACING_V2"] = "false"

    return {
        "tracing_enabled": tracing_enabled,
        "api_key_present": bool(langsmith_api_key),
        "project": os.getenv("LANGCHAIN_PROJECT", "Learning"),
        "validation_error": validation_error,
    }
