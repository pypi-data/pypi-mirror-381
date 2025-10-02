from http import HTTPStatus

from pydantic import validate_call


@validate_call
def get_http_status(status_code: int) -> tuple[HTTPStatus, bool]:
    """Get HTTP status code enum from integer value.

    Args:
        status_code (int, required): Status code for HTTP response: [100 <= status_code <= 599].

    Raises:
        ValueError: If status code is not in range [100 <= status_code <= 599].

    Returns:
        Tuple[HTTPStatus, bool]: Tuple of HTTP status code enum and boolean value if status code is known.
    """

    _http_status: HTTPStatus
    _is_known_status = False
    try:
        _http_status = HTTPStatus(status_code)
        _is_known_status = True
    except ValueError:
        if (100 <= status_code) and (status_code < 200):
            status_code = 100
        elif (200 <= status_code) and (status_code < 300):
            status_code = 200
        elif (300 <= status_code) and (status_code < 400):
            status_code = 304
        elif (400 <= status_code) and (status_code < 500):
            status_code = 400
        elif (500 <= status_code) and (status_code < 600):
            status_code = 500
        else:
            raise ValueError(
                f"`status_code` argument value '{status_code}' is invalid, must be in range 100-599!",
            )

        _http_status = HTTPStatus(status_code)

    return (_http_status, _is_known_status)


__all__ = [
    "get_http_status",
]
