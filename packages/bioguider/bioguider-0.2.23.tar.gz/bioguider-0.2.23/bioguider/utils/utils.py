import logging
import re
import subprocess
from typing import Optional
from pydantic import BaseModel
import tiktoken

from bioguider.utils.constants import DEFAULT_TOKEN_USAGE
logger = logging.getLogger(__name__)

def count_tokens(text: str, local_ollama: bool = False) -> int:
    """
    Count the number of tokens in a text string using tiktoken.

    Args:
        text (str): The text to count tokens for.
        local_ollama (bool, optional): Whether using local Ollama embeddings. Default is False.

    Returns:
        int: The number of tokens in the text.
    """
    try:
        if local_ollama:
            encoding = tiktoken.get_encoding("cl100k_base")
        else:
            encoding = tiktoken.encoding_for_model("text-embedding-3-small")

        return len(encoding.encode(text))
    except Exception as e:
        # Fallback to a simple approximation if tiktoken fails
        logger.warning(f"Error counting tokens with tiktoken: {e}")
        # Rough approximation: 4 characters per token
        return len(text) // 4


def run_command(command: list, cwd: str = None, timeout: int = None):
    """
    Run a shell command with optional timeout and return stdout, stderr, and return code.
    """
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired as e:
        return e.stdout or "", e.stderr or f"Command timed out after {timeout} seconds", -1

def escape_braces(text: str) -> str:
    # First replace single } not part of }} with }}
    text = re.sub(r'(?<!})}(?!})', '}}', text)
    # Then replace single { not part of {{
    text = re.sub(r'(?<!{){(?!{)', '{{', text)
    return text

def increase_token_usage(
    token_usage: Optional[dict] = None,
    incremental: dict = {**DEFAULT_TOKEN_USAGE},
):
    if token_usage is None:
        token_usage = {**DEFAULT_TOKEN_USAGE}
    token_usage["total_tokens"] += incremental["total_tokens"]
    token_usage["completion_tokens"] += incremental["completion_tokens"]
    token_usage["prompt_tokens"] += incremental["prompt_tokens"]

    return token_usage

def clean_action_input(action_input: str) -> str:
    replaced_input = ""

    while (True):
        replaced_input = action_input.strip()
        replaced_input = replaced_input.strip("`")
        replaced_input = replaced_input.strip('"')
        replaced_input = replaced_input.strip()
        replaced_input = replaced_input.strip("`")
        replaced_input = replaced_input.strip('"')
        replaced_input = replaced_input.strip()
        if (replaced_input == action_input):
            break
        action_input = replaced_input
    
    action_input = action_input.replace("'", '"')
    action_input = action_input.replace("`", '"')
    return action_input

# Convert BaseModel objects to dictionaries for JSON serialization
def convert_to_serializable(obj):
    if isinstance(obj, BaseModel):
        return obj.model_dump()
    elif hasattr(obj, 'model_dump'):
        return obj.model_dump()
    elif isinstance(obj, dict):
        return {k: convert_to_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, tuple):
        return [convert_to_serializable(item) for item in obj]
    else:
        return obj