"""Pydantic models for Model Hub API responses."""

from pydantic import BaseModel


class ModelVersionResponse(BaseModel):
    """
    Model version information.

    Attributes:
        version: Version identifier (e.g., '1.0.0', 'v2')
        description: Human-readable description of this version
    """

    version: str
    description: str


class ModelResponse(BaseModel):
    """
    Model information from Model Hub.

    Attributes:
        name: Model name
        versions: List of available versions for this model
    """

    name: str
    versions: list[ModelVersionResponse]


class ModelsListResponse(BaseModel):
    """
    Response from GET /api/models/list.

    Attributes:
        models: List of available models with their versions
    """

    models: list[ModelResponse]
