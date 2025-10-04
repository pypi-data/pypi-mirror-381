"""
DNN model subsystem for InvokeAI client using repository pattern.

This package provides DNN model discovery and access functionality following 
the repository pattern:
- DnnModel: Data model representing a deep neural network model
- DnnModelRepository: Manages model discovery and provides read-only access
- DnnModelType, BaseDnnModelType, DnnModelFormat: Enums for type safety

Note: DNN models are considered "static" resources in the current version,
so no ModelHandle class is needed yet (no runtime state management).
The term "dnn-model" is used to differentiate from Pydantic data models.
"""

from invokeai_py_client.dnn_model.dnn_model_types import (
    BaseDnnModelType,
    DnnModel,
    DnnModelFormat,
    DnnModelType,
)
from invokeai_py_client.dnn_model.dnn_model_repo import DnnModelRepository
from invokeai_py_client.dnn_model.dnn_model_models import (
    InstallJobStatus,
    ModelInstJobInfo,
    ModelManagerStats,
    HFLoginStatus,
    FoundModel,
    ModelInstallConfig,
)
from invokeai_py_client.dnn_model.model_inst_job_handle import ModelInstJobHandle
from invokeai_py_client.dnn_model.dnn_model_exceptions import (
    InvokeAIClientError,
    APIRequestError,
    ModelManagerError,
    ModelInstallStartError,
    ModelInstallJobFailed,
    ModelInstallTimeout,
)

__all__ = [
    "DnnModel",
    "DnnModelRepository",
    "DnnModelType",
    "BaseDnnModelType",
    "DnnModelFormat",
    # Model manager
    "InstallJobStatus",
    "ModelInstJobInfo",
    "ModelManagerStats",
    "HFLoginStatus",
    "FoundModel",
    "ModelInstallConfig",
    "ModelInstJobHandle",
    # Exceptions
    "InvokeAIClientError",
    "APIRequestError",
    "ModelManagerError",
    "ModelInstallStartError",
    "ModelInstallJobFailed",
    "ModelInstallTimeout",
]
