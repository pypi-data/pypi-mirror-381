# pylint: disable=missing-module-docstring, missing-class-docstring, line-too-long, invalid-name
from typing import List, Optional, Dict, Any, ClassVar, Literal
from pydantic import Field, BaseModel
from datetime import datetime, timezone
from ipulse_shared_base_ftredge import (
    AILearningParadigm,
    AIArchitectureFamily,
    RegressionAlgorithm,
    ClassificationAlgorithm,
    TimeSeriesAlgorithm,
    ObjectOverallStatus,
)
from .ai_io_format import AIModelIOCapabilities


class AIModelSpecification(BaseModel):
    """
    🏗️ AI MODEL SPECIFICATION - The Architectural Blueprint

    CORE CONCEPT:
    Defines the fundamental architecture and capabilities of an AI model - what it CAN do,
    not what it HAS done. This is the "specification sheet" that describes model capabilities,
    I/O requirements, and architectural constraints before any training or deployment occurs.

    KEY RELATIONSHIPS:
    • ONE specification → MULTIPLE model versions (AIModelVersion)
    • ONE specification → MULTIPLE training configurations  
    • ONE specification → MULTIPLE serving instances (via versions)
    • Specification defines CAPABILITIES, versions are IMPLEMENTATIONS

    GENERALIZATION STRATEGIES:
    • Specialized Models: Fixed input/output schemas, optimized for specific tasks
      - Example: Stock price predictor (AAPL OHLCV → price_target)
      - Static typing, predictable I/O, high performance for narrow use cases
    
    • Generalized Models: Dynamic I/O via prompting, adaptable to multiple tasks
      - Example: Foundation models (GPT-4, Gemini) with flexible capabilities
      - Runtime typing, morphic I/O (text → JSON → SQL → image → code)

    MULTIMODAL I/O CAPABILITIES:
    Specifications define supported modalities through AIModelIOCapabilities:
    • Input Modalities: TEXT, IMAGE, AUDIO, VIDEO, TABULAR, JSON_TEXT, etc.
    • Output Modalities: TEXT, STRUCTURED_JSON, IMAGE, AUDIO, etc.
    • Structure Levels: STRUCTURED, SEMI_STRUCTURED, UNSTRUCTURED
    • Content Dynamics: STATIC, SEQUENCE, TIMESERIES, STREAMING

    EXTERNAL MODEL SUPPORT:
    • Foundation Models: GPT-4, Gemini Pro, Claude-3 with API configurations
    • Managed Services: BigQuery ML, Vertex AI, SageMaker, Databricks ML
    • API Integration: Authentication, endpoints, rate limits, fallback strategies

    TARGET SPECIFICATION SYSTEM:
    Flexible criteria for defining prediction scope:
    ```json
    {
        "domain": ["fincore_market_assets"],
        "asset_class": ["equity", "crypto"], 
        "market_cap_min": 1000000000,
        "specific_object_ids": ["AAPL", "GOOGL"]
    }
    ```

    ARCHITECTURAL FAMILIES:
    • Regression: Continuous value prediction with confidence intervals
    • Classification: Category prediction with probability distributions  
    • Time Series: Temporal pattern analysis and forecasting
    • Foundation Model: Multi-task capability via natural language interfaces

    LIFECYCLE INTEGRATION:
    Specifications flow into training configurations → training runs → model versions → serving instances,
    providing the architectural foundation for the entire ML pipeline while maintaining clear separation
    of concerns between design (specification) and implementation (versions).
    """

    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    VERSION: ClassVar[int] = 3
    DOMAIN: ClassVar[str] = "dp_oracle_fincore_prediction"
    OBJ_REF: ClassVar[str] = "aimodelspec"

    # Core identification
    model_spec_id: str = Field(..., description="Unique identifier for this AI model specification")
    model_spec_name: str = Field(..., description="Human-readable name of the AI model specification")
    pulse_status: ObjectOverallStatus = Field(default=ObjectOverallStatus.ACTIVE, description="Status of this model specification: ACTIVE (in use), INACTIVE (not in use), DRAFT (being developed), RETIRED (permanently discontinued)")

    # Model classification
    model_generalization_level: Literal["specialized", "generalized"] = Field(..., description="'specialized' for fixed I/O models, 'generalized' for foundation models")
    
    # Target specification (for specialized models)
    target_object_id: Optional[str] = Field(None, description="In highly specialized models: single object ID this model targets, e.g., 'AAPL' (NULL for generalized models)")
    target_record_type: Optional[str] = Field(None, description="In highly specialized models: record type of this model's targets, e.g., 'eod_adjc', 'intraday_adjc', 'eod_vol'")

    # I/O Capabilities (single objects stored as JSON in BigQuery)
    input_capabilities: Optional[AIModelIOCapabilities] = Field(None, description="Input format capabilities and constraints")
    output_capabilities: Optional[AIModelIOCapabilities] = Field(None, description="Output format capabilities and constraints")

    # Model source and architecture
    model_source: Literal["internal", "external_foundational", "external_service"] = Field(..., description="internal: trained by us, external_foundational: like GPT-4, external_service: managed service")
    model_author: str = Field(..., description="Author or team responsible for the model")
    model_provider_organization: str = Field(..., description="Comma-separated list of provider organizations (e.g., OpenAI, Google, Anthropic)")
    model_license: Optional[str] = Field(None, description="License under which the model is released")
    model_rights_description: Optional[str] = Field(None, description="Description of rights associated with the model")

    # --- Training & Features ---
    learning_paradigm: AILearningParadigm = Field(..., description="Learning paradigm: supervised, unsupervised, reinforcement, etc.")
    ai_architecture_family: AIArchitectureFamily = Field(..., description="AI architecture family: regression, classification, time_series_forecasting, foundation_model, etc.")
    algorithm: Optional[str |
        RegressionAlgorithm |
        ClassificationAlgorithm |
        TimeSeriesAlgorithm
    ] = Field(None, description="The underlying algorithm used. For foundational models, this represents their core architecture (e.g., TRANSFORMER for GPT).")
    # algorithm: Optional[str] = Field(None, description="Specific algorithm used (varies by architecture family)")

    foundation_model_type: Optional[str] = Field(None, description="Model family, e.g., 'gpt-4', 'gemini-pro', 'claude-3', applicable for foundational models only.")
    external_managed_model_service_name: Optional[str] = Field(None, description="External service name (e.g., 'bigquery_ml', 'bigquery_ai', 'vertex_ai', 'sagemaker', 'databricks_ml').")

    # Development details
    model_development_framework: Optional[Dict[str, Any]] = Field(None, description="Information about the model framework, e.g., {'framework': 'TensorFlow', 'version': '2.14', 'gpu_support': True}.")
    model_description: Optional[str] = Field(None, description="Detailed description of the model, purpose, and architecture")
    model_overall_pulse_performance_score: Optional[float] = Field(None, description="A single overall performance score for the model.")
    parameters_count: Optional[int] = Field(None, description="Number of parameters in the model for complexity assessment")
    hyperparameters_schema: Optional[Dict[str, Any]] = Field(None, description="The hyperparameters used to train the model, e.g., {'learning_rate': 0.001, 'batch_size': 32, 'epochs': 100}.")
    model_complexity_score: Optional[float] = Field(None, description="Complexity score for model comparison and resource planning")

    model_features: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional model modes/features: {'deep_thinking':'description....'', 'function_calling':'...', 'internet_browsing':'...', 'code_execution':'...', 'vision_analysis':'...', 'multimodal_reasoning':'...'}")

    # --- USE CASES--- # Below is COMMENTED OUT , BECAUSE THERE ARE POTENTIALLY MANY VERSIONS FOR A SINGLE MODEL
    
    notes: Optional[str] = Field(None, description="Additional notes about this model specification")
    strengths: Optional[str] = Field(None, description="Description of the model specification strengths")
    weaknesses: Optional[str] = Field(None, description="Description of the model specification weaknesses")
    recommended_use_cases: Optional[str] = Field(None, description="Comma-separated list of recommended use cases")
    recommended_consumers: Optional[str] = Field(None, description="Comma-separated list of recommended consumers (trading_system, retail_customer, financial_analyst, financial_advisor, enterprise_customer, etc.)")
    model_conceived_on: Optional[datetime] = Field(..., description="The timestamp when the model was created.")
    tags: Dict[str, str] = Field(default_factory=dict, description="Tags for categorization, e.g., {'environment': 'production', 'team': 'ml-ops'}.")

    # --- Namespace and Identity ---
    pulse_namespace: Optional[str] = Field(None, description="Namespace for this AI model specification.")
    namespace_id_seed_phrase: Optional[str] = Field(None, description="Seed phrase used for namespace-based UUID generation.")

    # Audit fields - created fields are frozen after creation, updated fields are mutable
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)
    created_by: Optional[str] = Field(..., frozen=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(...)



    

    