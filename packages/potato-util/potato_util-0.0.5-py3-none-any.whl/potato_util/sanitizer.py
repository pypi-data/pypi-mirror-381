import re
import html
from urllib.parse import quote

from pydantic import validate_call, AnyHttpUrl

from .constants import (
    SPECIAL_CHARS_BASE_REGEX,
    SPECIAL_CHARS_LOW_REGEX,
    SPECIAL_CHARS_MEDIUM_REGEX,
    SPECIAL_CHARS_HIGH_REGEX,
    SPECIAL_CHARS_STRICT_REGEX,
)


@validate_call
def escape_html(val: str) -> str:
    """Escape HTML characters.

    Args:
        val (str, required): String to escape.

    Returns:
        str: Escaped string.
    """

    val = val.strip()
    _escaped = html.escape(val)
    return _escaped


@validate_call
def escape_url(val: AnyHttpUrl | str) -> str:
    """Escape URL characters.

    Args:
        val (AnyHttpUrl, required): String to escape.

    Returns:
        str: Escaped string.
    """

    if isinstance(val, str):
        val = AnyHttpUrl(val)

    _escaped = quote(str(val))
    return _escaped


@validate_call
def sanitize_special_chars(val: str, mode: str = "LOW") -> str:
    """Sanitize special characters.
    Available modes:
        - "BASE" or "HTML": Basic HTML special characters.
        - "LOW": Low-risk special characters.
        - "MEDIUM": Medium-risk special characters.
        - "HIGH", "SCRIPT", or "SQL": High-risk special characters.
        - "STRICT": Strict mode, removes most special characters.

    Args:
        val  (str, required): String to sanitize.
        mode (str, optional): Sanitization mode. Defaults to "LOW".

    Raises:
        ValueError: If `mode` argument value is invalid.

    Returns:
        str: Sanitized string.
    """

    _pattern = r""
    mode = mode.upper().strip()
    if (mode == "BASE") or (mode == "HTML"):
        _pattern = SPECIAL_CHARS_BASE_REGEX
    elif mode == "LOW":
        _pattern = SPECIAL_CHARS_LOW_REGEX
    elif mode == "MEDIUM":
        _pattern = SPECIAL_CHARS_MEDIUM_REGEX
    elif (mode == "HIGH") or (mode == "SCRIPT") or (mode == "SQL"):
        _pattern = SPECIAL_CHARS_HIGH_REGEX
    elif mode == "STRICT":
        _pattern = SPECIAL_CHARS_STRICT_REGEX
    else:
        raise ValueError(f"`mode` argument value '{mode}' is invalid!")

    _sanitized = re.sub(pattern=_pattern, repl="", string=val)
    return _sanitized


__all__ = [
    "escape_html",
    "escape_url",
    "sanitize_special_chars",
]
