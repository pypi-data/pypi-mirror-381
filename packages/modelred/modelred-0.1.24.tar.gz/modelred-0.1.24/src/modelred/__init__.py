import logging

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Union

__version__ = "0.1.24"

from .client import AsyncModelRedClient, ModelRedClient
from .config import DEFAULT_BASE_URL, load_settings
from .exceptions import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    ModelRedError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
    SubscriptionLimitError,
    ValidationError,
)
from .resources.assessments import (
    Assessment as _ResourceAssessment,
    AssessmentPriority as _ResourcePriority,
    AssessmentStatus as _ResourceStatus,
)
from .resources.models import Model as _ResourceModel
from .resources.probes import Probe as Probe, ProbeIndex as ProbesIndex

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
logger = logging.getLogger("modelred")
if not logger.handlers:
    h = logging.StreamHandler()
    h.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(h)
logger.setLevel(logging.INFO)

# -----------------------------------------------------------------------------
# Constants / Enums
# -----------------------------------------------------------------------------
BASE_URL = DEFAULT_BASE_URL


class ModelProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    HUGGINGFACE = "huggingface"
    REST = "rest"
    BEDROCK = "bedrock"
    SAGEMAKER = "sagemaker"
    GOOGLE = "google"


AssessmentStatus = _ResourceStatus
Priority = _ResourcePriority


# -----------------------------------------------------------------------------
# Data classes
# -----------------------------------------------------------------------------
@dataclass
class Model:
    id: str
    modelId: str
    provider: str
    modelName: Optional[str]
    displayName: str
    description: Optional[str]
    isActive: bool
    lastTested: Optional[datetime]
    testCount: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    createdByUser: Optional[Dict[str, Any]] = None


@dataclass
class Assessment:
    id: str
    modelId: str
    status: AssessmentStatus
    testTypes: List[str]
    priority: Priority
    progress: int = 0
    results: Optional[Dict[str, Any]] = None
    errorMessage: Optional[str] = None
    createdAt: Optional[datetime] = None
    completedAt: Optional[datetime] = None
    estimatedDuration: Optional[int] = None
    detailedReport: Optional[Dict[str, Any]] = None


# -----------------------------------------------------------------------------
# Provider config helpers
# -----------------------------------------------------------------------------
class ProviderConfig:
    """Factory methods for creating provider-specific configuration dictionaries.

    Each provider has different requirements:
    - OpenAI: api_key, model_name, optional organization
    - Anthropic: api_key, model_name
    - Azure: api_key, endpoint, deployment_name, api_version
    - OpenRouter: api_key, model_name, optional base_url
    - Google (Gemini): api_key, model_name
    - Grok (xAI): api_key, model_name
    - HuggingFace: model_name, optional api_key
    - REST: uri, optional api_key and headers
    - Bedrock/Sagemaker: AWS credentials
    """

    @staticmethod
    def openai(
        api_key: str,
        model_name: str = "gpt-4o-mini",
        organization: Optional[str] = None,
    ) -> Dict[str, Any]:
        """OpenAI configuration.

        Args:
            api_key: OpenAI API key (starts with sk-)
            model_name: Model identifier (e.g. "gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo")
            organization: Optional organization ID
        """
        cfg = {"api_key": api_key, "model_name": model_name}
        if organization:
            cfg["organization"] = organization
        return cfg

    @staticmethod
    def anthropic(
        api_key: str, model_name: str = "claude-3-5-sonnet-20241022"
    ) -> Dict[str, Any]:
        """Anthropic Claude configuration.

        Args:
            api_key: Anthropic API key
            model_name: Model identifier (e.g. "claude-3-5-sonnet-20241022", "claude-3-5-haiku-20241022")
        """
        return {"api_key": api_key, "model_name": model_name}

    @staticmethod
    def azure(
        api_key: str,
        endpoint: str,
        deployment_name: str,
        api_version: str = "2024-06-01",
    ) -> Dict[str, Any]:
        """Azure OpenAI configuration.

        Args:
            api_key: Azure OpenAI API key
            endpoint: Azure OpenAI endpoint URL (e.g. "https://YOUR_RESOURCE.openai.azure.com")
            deployment_name: Azure deployment name
            api_version: Azure API version (default: "2024-06-01")
        """
        return {
            "api_key": api_key,
            "endpoint": endpoint,
            "deployment_name": deployment_name,
            "api_version": api_version,
        }

    @staticmethod
    def openrouter(
        api_key: str,
        model_name: str,
        base_url: str = "https://openrouter.ai/api/v1",
    ) -> Dict[str, Any]:
        """OpenRouter configuration.

        Args:
            api_key: OpenRouter API key
            model_name: Model identifier (e.g. "anthropic/claude-3.5-sonnet", "google/gemini-pro-1.5")
            base_url: OpenRouter API base URL (default: "https://openrouter.ai/api/v1")
        """
        return {
            "api_key": api_key,
            "model_name": model_name,
            "base_url": base_url,
        }

    @staticmethod
    def grok(
        api_key: str,
        model_name: str = "grok-beta",
    ) -> Dict[str, Any]:
        """xAI Grok configuration.

        Args:
            api_key: xAI API key
            model_name: Model identifier (default: "grok-beta")
        """
        return {
            "api_key": api_key,
            "model_name": model_name,
        }

    @staticmethod
    def google(
        model_name: str,
        api_key: str,
        *,
        generation_config: Optional[Dict[str, Any]] = None,
        safety_settings: Optional[List[Dict[str, Any]]] = None,
        # legacy args kept for compatibility but ignored:
        project_id: Optional[str] = None,
        location: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Google Gemini (Developer API) configuration.

        Args:
            model_name: Model identifier (e.g. "gemini-2.0-flash-exp", "gemini-1.5-pro")
            api_key: Google AI Studio / Developer API key
            generation_config: Optional generation configuration dict
            safety_settings: Optional safety settings list

        Notes:
            - Vertex AI params (project_id, location) are ignored in current version
        """
        if not api_key:
            raise ValidationError("Google (Developer API) requires api_key")

        # Gentle warning if legacy Vertex hints are supplied
        if project_id or location:
            logger.warning(
                "ProviderConfig.google: ignoring Vertex params (project_id/location) "
                "because SDK is in Developer API mode."
            )

        cfg: Dict[str, Any] = {
            "model_name": model_name,
            "api_key": api_key,
        }
        if generation_config is not None:
            cfg["generation_config"] = generation_config
        if safety_settings is not None:
            cfg["safety_settings"] = safety_settings
        return cfg


# -----------------------------------------------------------------------------
# Base client
# -----------------------------------------------------------------------------
class ModelRed:
    """Synchronous ModelRed SDK client.

    Security features:
    - DELETE operations are disabled for user safety
    - Base URL is only configurable via MODELRED_BASE_URL environment variable
    - API keys must be provided explicitly or via MODELRED_API_KEY environment variable
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        timeout: int = 30,
        *,
        _client: Optional[ModelRedClient] = None,
    ) -> None:
        """Initialize ModelRed client.

        Args:
            api_key: Your ModelRed API key (or set MODELRED_API_KEY environment variable)
            timeout: Request timeout in seconds (default: 30)

        Security Note:
            The base_url is ONLY configurable via MODELRED_BASE_URL environment variable.
            This prevents malicious code from redirecting your API traffic.
        """
        settings = load_settings(timeout=timeout)
        self._client = _client or ModelRedClient(api_key=api_key, settings=settings)
        self.timeout = timeout
        self.logger = logger
        self.api_key = self._client.api_key

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": f"ModelRed-PythonSDK/{__version__}",
        }

    # Models
    def create_model(
        self,
        *,
        modelId: str,
        provider: Union[str, ModelProvider],
        displayName: str,
        providerConfig: Dict[str, Any],
        description: Optional[str] = None,
    ) -> Model:
        """Create a new model configuration.

        Args:
            modelId: Unique identifier for this model
            provider: Model provider (use ModelProvider enum)
            displayName: Human-readable display name
            providerConfig: Provider-specific configuration (use ProviderConfig helper methods)
            description: Optional model description

        Returns:
            Created Model object

        Example:
            model = client.create_model(
                modelId="my-gpt4",
                provider=ModelProvider.OPENAI,
                displayName="GPT-4",
                providerConfig=ProviderConfig.openai(
                    api_key=os.environ["OPENAI_API_KEY"],
                    model_name="gpt-4o-mini"
                )
            )
        """
        provider_value = (
            provider.value if isinstance(provider, ModelProvider) else str(provider)
        )
        resource = self._client.models.create(
            model_id=modelId,
            provider=provider_value,
            display_name=displayName,
            provider_config=providerConfig,
            description=description,
        )
        return _to_legacy_model(resource)

    def list_models(self) -> List[Model]:
        """List all models in your organization.

        Returns:
            List of Model objects
        """
        return [_to_legacy_model(m) for m in self._client.models.list()]

    def get_model(self, model_identifier: str) -> Model:
        """Retrieve a specific model by ID or modelId.

        Args:
            model_identifier: Model ID or modelId

        Returns:
            Model object
        """
        resource = self._client.models.retrieve(model_identifier)
        return _to_legacy_model(resource)

    # Assessments
    def create_assessment(
        self,
        *,
        model: str,
        test_types: List[str],
        priority: Union[str, Priority] = Priority.NORMAL,
    ) -> Assessment:
        """Create a new security assessment.

        Args:
            model: Model ID or modelId to assess
            test_types: List of probe keys to run (get from list_probes())
            priority: Assessment priority (default: Priority.NORMAL)

        Returns:
            Created Assessment object (status will be QUEUED initially)

        Example:
            assessment = client.create_assessment(
                model="my-gpt4",
                test_types=["reverse_psychology", "role_swap", "hypothetical_probe"],
                priority=Priority.NORMAL
            )
        """
        priority_value = _normalise_priority(priority)
        resource = self._client.assessments.create(
            model=model,
            test_types=test_types,
            priority=priority_value,
        )
        return _to_legacy_assessment(resource)

    def get_assessment(self, assessment_id: str) -> Assessment:
        """Retrieve assessment status and results.

        Args:
            assessment_id: Assessment ID

        Returns:
            Assessment object with current status and results (if completed)
        """
        resource = self._client.assessments.retrieve(assessment_id)
        return _to_legacy_assessment(resource)

    def list_assessments(self, limit: Optional[int] = None) -> List[Assessment]:
        """List recent assessments.

        Args:
            limit: Maximum number of assessments to return (optional)

        Returns:
            List of Assessment objects
        """
        resources = self._client.assessments.list(limit=limit)
        return [_to_legacy_assessment(a) for a in resources]

    def wait_for_completion(
        self,
        assessment_id: str,
        *,
        timeout_minutes: int = 60,
        poll_interval: int = 10,
        progress_callback: Optional[Callable[[Assessment], None]] = None,
    ) -> Assessment:
        """Wait for assessment to complete, polling for status updates.

        Args:
            assessment_id: Assessment ID
            timeout_minutes: Maximum time to wait (default: 60)
            poll_interval: Seconds between status checks (default: 10)
            progress_callback: Optional callback function called on status changes

        Returns:
            Completed Assessment object with results

        Example:
            def on_progress(assessment):
                print(f"Status: {assessment.status} - Progress: {assessment.progress}%")

            result = client.wait_for_completion(
                assessment_id,
                timeout_minutes=15,
                progress_callback=on_progress
            )
        """
        wrapped = _wrap_sync_callback(progress_callback)
        resource = self._client.assessments.wait_for_completion(
            assessment_id,
            timeout_seconds=timeout_minutes * 60,
            poll_interval=poll_interval,
            progress_callback=wrapped,
        )
        return _to_legacy_assessment(resource)

    # Probes
    def list_probes(
        self,
        *,
        category: Optional[str] = None,
    ) -> ProbesIndex:
        """List all security probes available for your subscription tier.

        This method automatically returns probes based on your organization's
        subscription level. No need to specify tier - it's determined server-side.

        Args:
            category: Optional category filter (e.g. "universal", "medical_ethics",
                     "legal_ethics", "financial_compliance", "cyber_operations")

        Returns:
            ProbesIndex containing available probes and metadata

        Example:
            # Get all available probes
            probes = client.list_probes()

            # Filter by category
            medical_probes = client.list_probes(category="medical_ethics")

            # Use probe keys in assessment
            probe_keys = [p.key for p in probes.probes[:5]]
            assessment = client.create_assessment(
                model="my-model",
                test_types=probe_keys
            )
        """
        # SECURITY: tier filtering is done server-side based on authenticated user
        # Users cannot access probes outside their subscription tier
        return self._client.probes.list(
            category=category,
            tier=None,  # Server determines tier from API key
            severity=None,
        )

    def redacted_api_key(self) -> str:
        return self._client.redacted_api_key()

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ModelRed":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


class AsyncModelRed:
    """Async ModelRed SDK client.

    Security features:
    - DELETE operations are disabled for user safety
    - Base URL is only configurable via MODELRED_BASE_URL environment variable
    - API keys must be provided explicitly or via MODELRED_API_KEY environment variable
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        timeout: int = 30,
        *,
        _client: Optional[AsyncModelRedClient] = None,
    ) -> None:
        """Initialize async ModelRed client.

        Args:
            api_key: Your ModelRed API key (or set MODELRED_API_KEY environment variable)
            timeout: Request timeout in seconds (default: 30)

        Security Note:
            The base_url is ONLY configurable via MODELRED_BASE_URL environment variable.
            This prevents malicious code from redirecting your API traffic.
        """
        settings = load_settings(timeout=timeout)
        self._client = _client or AsyncModelRedClient(
            api_key=api_key, settings=settings
        )
        self.timeout = timeout
        self.logger = logger
        self.api_key = self._client.api_key

    # Models
    async def create_model(
        self,
        *,
        modelId: str,
        provider: Union[str, ModelProvider],
        displayName: str,
        providerConfig: Dict[str, Any],
        description: Optional[str] = None,
    ) -> Model:
        """Create a new model configuration (async).

        See ModelRed.create_model() for full documentation.
        """
        provider_value = (
            provider.value if isinstance(provider, ModelProvider) else str(provider)
        )
        resource = await self._client.models.create(
            model_id=modelId,
            provider=provider_value,
            display_name=displayName,
            provider_config=providerConfig,
            description=description,
        )
        return _to_legacy_model(resource)

    async def list_models(self) -> List[Model]:
        """List all models in your organization (async)."""
        resources = await self._client.models.list()
        return [_to_legacy_model(m) for m in resources]

    async def get_model(self, model_identifier: str) -> Model:
        """Retrieve a specific model by ID or modelId (async)."""
        resource = await self._client.models.retrieve(model_identifier)
        return _to_legacy_model(resource)

    # Assessments
    async def create_assessment(
        self,
        *,
        model: str,
        test_types: List[str],
        priority: Union[str, Priority] = Priority.NORMAL,
    ) -> Assessment:
        """Create a new security assessment (async).

        See ModelRed.create_assessment() for full documentation.
        """
        priority_value = _normalise_priority(priority)
        resource = await self._client.assessments.create(
            model=model,
            test_types=test_types,
            priority=priority_value,
        )
        return _to_legacy_assessment(resource)

    async def get_assessment(self, assessment_id: str) -> Assessment:
        """Retrieve assessment status and results (async)."""
        resource = await self._client.assessments.retrieve(assessment_id)
        return _to_legacy_assessment(resource)

    async def list_assessments(self, limit: Optional[int] = None) -> List[Assessment]:
        """List recent assessments (async)."""
        resources = await self._client.assessments.list(limit=limit)
        return [_to_legacy_assessment(a) for a in resources]

    async def wait_for_completion(
        self,
        assessment_id: str,
        *,
        timeout_minutes: int = 60,
        poll_interval: int = 10,
        progress_callback: Optional[Callable[[Assessment], None]] = None,
    ) -> Assessment:
        """Wait for assessment to complete (async).

        See ModelRed.wait_for_completion() for full documentation.
        """
        wrapped = _wrap_async_callback(progress_callback)
        resource = await self._client.assessments.wait_for_completion(
            assessment_id,
            timeout_seconds=timeout_minutes * 60,
            poll_interval=poll_interval,
            progress_callback=wrapped,
        )
        return _to_legacy_assessment(resource)

    async def list_probes(
        self,
        *,
        category: Optional[str] = None,
    ) -> ProbesIndex:
        """List all security probes available for your subscription tier (async).

        See ModelRed.list_probes() for full documentation.
        """
        # SECURITY: tier filtering is done server-side based on authenticated user
        return await self._client.probes.list(
            category=category,
            tier=None,  # Server determines tier from API key
            severity=None,
        )

    def redacted_api_key(self) -> str:
        return self._client.redacted_api_key()

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AsyncModelRed":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._client.__aexit__(exc_type, exc, tb)


def _normalise_priority(priority: Union[str, Priority]) -> Priority:
    if isinstance(priority, Priority):
        return priority
    return Priority(str(priority).lower())


def _to_legacy_model(model: _ResourceModel) -> Model:
    return Model(
        id=model.id,
        modelId=model.model_id,
        provider=model.provider,
        modelName=model.model_name,
        displayName=model.display_name,
        description=model.description,
        isActive=model.is_active,
        lastTested=model.last_tested,
        testCount=model.test_count,
        createdAt=model.created_at,
        updatedAt=model.updated_at,
        createdByUser=None,
    )


def _to_legacy_assessment(assessment: _ResourceAssessment) -> Assessment:
    return Assessment(
        id=assessment.id,
        modelId=assessment.model_id,
        status=assessment.status,
        testTypes=assessment.test_types,
        priority=assessment.priority,
        progress=assessment.progress,
        results=None,
        errorMessage=None,
        createdAt=assessment.created_at,
        completedAt=assessment.completed_at,
        estimatedDuration=None,
        detailedReport=assessment.detailed_report,
    )


def _wrap_sync_callback(
    callback: Optional[Callable[[Assessment], None]],
) -> Optional[Callable[[_ResourceAssessment], None]]:
    if callback is None:
        return None

    def _inner(resource_assessment: _ResourceAssessment) -> None:
        callback(_to_legacy_assessment(resource_assessment))

    return _inner


def _wrap_async_callback(
    callback: Optional[Callable[[Assessment], None]],
) -> Optional[Callable[[_ResourceAssessment], None]]:
    if callback is None:
        return None

    def _inner(resource_assessment: _ResourceAssessment) -> None:
        callback(_to_legacy_assessment(resource_assessment))

    return _inner


# -----------------------------------------------------------------------------
# Public exports
# -----------------------------------------------------------------------------
__all__ = [
    "ModelRed",
    "AsyncModelRed",
    "ModelRedClient",
    "AsyncModelRedClient",
    "Model",
    "Assessment",
    "ModelProvider",
    "AssessmentStatus",
    "Priority",
    "ProviderConfig",
    # Exceptions
    "ModelRedError",
    "AuthenticationError",
    "AuthorizationError",
    "SubscriptionLimitError",
    "ValidationError",
    "NotFoundError",
    "ConflictError",
    "RateLimitError",
    "ServerError",
    "NetworkError",
]
