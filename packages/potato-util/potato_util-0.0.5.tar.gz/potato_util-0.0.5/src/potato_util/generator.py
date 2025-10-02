import uuid
import string
import secrets

from pydantic import validate_call

from .dt import now_ts


@validate_call
def gen_unique_id(prefix: str = "") -> str:
    """Generate unique ID. Format: '{prefix}{datetime}_{uuid4}'.

    Args:
        prefix (str, optional): Prefix of ID. Defaults to ''.

    Raises:
        ValueError: If `prefix` length is greater than 32.

    Returns:
        str: Unique ID.
    """

    prefix = prefix.strip()
    if 32 < len(prefix):
        raise ValueError(
            f"`prefix` argument length {len(prefix)} is too long, must be less than or equal to 32!",
        )

    _id = str(f"{prefix}{now_ts()}_{uuid.uuid4().hex}").lower()
    return _id


@validate_call
def gen_random_string(length: int = 16, is_alphanum: bool = True) -> str:
    """Generate secure random string.

    Args:
        length      (int , optional): Length of random string. Defaults to 16.
        is_alphanum (bool, optional): If True, generate only alphanumeric string. Defaults to True.

    Raises:
        ValueError: If `length` is less than 1.

    Returns:
        str: Generated random string.
    """

    if length < 1:
        raise ValueError(
            f"`length` argument value {length} is too small, must be greater than or equal to 1!",
        )

    _base_chars = string.ascii_letters + string.digits
    if not is_alphanum:
        _base_chars += string.punctuation

    _random_str = "".join(secrets.choice(_base_chars) for _i in range(length))
    return _random_str


__all__ = [
    "gen_unique_id",
    "gen_random_string",
]
