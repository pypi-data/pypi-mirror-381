"""Custom exceptions raised by the Simulacrum SDK."""

from typing import Dict, Type


class SimulacrumError(Exception):
    """Base exception for all SDK errors."""


class AuthError(SimulacrumError):
    """Raised when authentication with the API fails."""


class ApiKeyExpiredError(SimulacrumError):
    """Raised when the API key has expired."""


class ApiKeyInactiveError(SimulacrumError):
    """Raised when the API key has been deactivated."""


class ApiKeyInvalidError(AuthError):
    """Raised when the API key is not recognised."""


class ForecastAlreadyRunningError(SimulacrumError):
    """Raised when a forecast job is already in progress."""


class InvalidRequestError(SimulacrumError):
    """Raised when the request payload is malformed."""


class QuotaExceededError(SimulacrumError):
    """Raised when the API usage quota has been exhausted."""


class ApiError(SimulacrumError):
    """Catch-all for unclassified API errors."""


ERROR_CODE_MAP: Dict[str, Type[SimulacrumError]] = {
    "API_KEY_EXPIRED": ApiKeyExpiredError,
    "API_KEY_INVALID": ApiKeyInvalidError,
    "API_KEY_INACTIVE": ApiKeyInactiveError,
    "API_USAGE_LIMIT": QuotaExceededError,
    "REQUEST_INVALID": InvalidRequestError,
    "FORECAST_ALREADY_RUNNING": ForecastAlreadyRunningError,
}
