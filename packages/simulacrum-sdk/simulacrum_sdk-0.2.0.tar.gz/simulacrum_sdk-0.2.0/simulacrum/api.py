"""Low-level HTTP helpers used by the Simulacrum client."""

from typing import Any, Dict, Mapping, Optional

import requests

from simulacrum.exceptions import ApiError, AuthError, ERROR_CODE_MAP


def send_request(method: str, url: str, headers: Mapping[str, str], json: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    """Execute an HTTP request against the Simulacrum API and handle common errors.

    Args:
        method (str): HTTP method to invoke (``"GET"``, ``"POST"``, ...).
        url (str): Fully-qualified endpoint URL.
        headers (Mapping[str, str]): HTTP headers that include authorization and content type.
        json (Mapping[str, Any] | None): JSON-serialisable payload for the request body.

    Returns:
        dict[str, Any]: Parsed JSON payload returned by the API.

    Raises:
        AuthError: Raised when the API reports an authentication failure.
        ApiError: Raised for all other non-success responses or malformed data.
    """
    response = requests.request(method=method, url=url, headers=dict(headers), json=json)

    if not response.ok:
        try:
            data: Dict[str, Any] = response.json()
            error_code: Optional[str] = data.get("error_code")
            message: str = data.get("message", "Unknown error")

            if error_code in ERROR_CODE_MAP:
                raise ERROR_CODE_MAP[error_code](message)

            if response.status_code == 401:
                raise AuthError(message)

            raise ApiError(f"API error {response.status_code}: {message}")

        except ValueError as exc:
            raise ApiError(f"Unexpected API error: {response.text}") from exc

    try:
        return response.json()  # type: ignore[return-value]
    except ValueError as exc:  # requests raises ValueError for JSON decode errors
        raise ApiError(f"Failed to parse response JSON: {exc}") from exc
