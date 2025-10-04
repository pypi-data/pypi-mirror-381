"""Data models that map request and response payloads for the Simulacrum API."""

from datetime import datetime
from typing import List, Optional, Sequence, Union
from enum import Enum

import numpy as np
from pydantic import BaseModel, field_validator, Field, constr


class ForecastRequest(BaseModel):
    """Payload submitted to the Simulacrum forecast endpoint.

    Attributes:
        series (list[float]): Historical observations used as forecast input.
        horizon (int): Number of future periods to predict.
        model (str | None): Identifier of the forecasting model, defaults to ``"default"``.

    Example:
        >>> from simulacrum.models import ForecastRequest
        >>> payload = ForecastRequest(series=[1.0, 2.0, 3.0], horizon=2, model="default")
        >>> payload.model_dump()
        {'series': [1.0, 2.0, 3.0], 'horizon': 2, 'model': 'default'}
    """

    series: List[float]
    horizon: int
    model: Optional[str] = "default"

    @field_validator("series", mode="before")
    @classmethod
    def _ensure_series_list(cls, value: Union[np.ndarray, Sequence[float]]) -> List[float]:  # type: ignore[override]
        """Normalise the series field to ``list[float]``.

        Args:
            value (numpy.ndarray | Sequence[float]): Incoming value from caller.

        Returns:
            list[float]: Serialisable list of floats.
        """
        if isinstance(value, np.ndarray):
            return value.astype(float).tolist()
        return list(value)


class ForecastResponse(BaseModel):
    """Forecast output returned by the API.

    Attributes:
        forecast (list[float]): Forecasted values returned by the service.
        model_used (str): Identifier of the model the backend selected.

    Example:
        >>> from simulacrum.models import ForecastResponse
        >>> response = ForecastResponse(forecast=[4.2, 4.8], model_used="default")
        >>> response.get_forecast().tolist()
        [4.2, 4.8]
    """

    forecast: List[float]

    def get_forecast(self) -> np.ndarray:
        """Return forecast values as a numpy array for downstream processing.

        Returns:
            numpy.ndarray: Forecast data cast to an array of floats.
        """
        return np.array(self.forecast, dtype=float)


class ApiKeyStatus(str, Enum):
    """Possible statuses for an API key."""

    active = "active"
    deprecated = "deprecated"
    disabled = "disabled"


class ApiKeyStatusHistoryEntry(BaseModel):
    """API key status history entry."""

    status: ApiKeyStatus
    changed_at: datetime

    class Config:
        extra = "forbid"


class ValidateAPIKeyResponse(BaseModel):
    """Structured representation of an API key validation response."""

    valid: bool
    key_id: constr(pattern=r"^[A-Za-z0-9]+$")
    status: ApiKeyStatus
    env: constr(pattern=r"^(live|test)$")
    project_id: str
    organization_id: str
    user_id: str
    product_id: str
    name: constr(min_length=1, max_length=255)
    expires_at: Optional[datetime] = None
    rate_limit_per_minute: int = Field(ge=1)
    rate_limit_per_hour: int = Field(ge=1)

    class Config:
        extra = "forbid"
