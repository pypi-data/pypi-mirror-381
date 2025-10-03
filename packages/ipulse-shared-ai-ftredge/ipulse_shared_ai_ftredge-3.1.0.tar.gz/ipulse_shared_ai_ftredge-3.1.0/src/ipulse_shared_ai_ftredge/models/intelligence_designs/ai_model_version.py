# pylint: disable=missing-module-docstring, missing-class-docstring, line-too-long, invalid-name
from typing import List, Optional, Dict, ClassVar
from pydantic import Field, BaseModel
from datetime import datetime, timezone
from ipulse_shared_base_ftredge import AIModelStatus, ObjectOverallStatus


class AIModelVersion(BaseModel):
    """
    📦 AI MODEL VERSION - The Trained Implementation

    CORE CONCEPT:
    Represents a specific, trained instance of an AI model that is ready for deployment.
    This is the successful result of executing a training configuration against a model 
    specification, producing a versioned artifact ready for serving.

    KEY RELATIONSHIPS:
    • ONE model specification (AIModelSpecification) → MULTIPLE model versions
    • ONE training configuration → MULTIPLE model versions (over time)
    • ONE training run → ZERO or ONE model version (if training succeeded)
    • ONE model version → MULTIPLE serving instances (AIModelServingInstance)

    VERSION LINEAGE & EVOLUTION:
    Model versions form evolutionary lineages through parent_version_id:
    • Base Model: v1.0.0 (initial training from specification)
    • Retrained: v1.1.0 → v1.2.0 → v1.3.0 (scheduled retraining cycles)
    • Fine-tuned: v1.1.1 → v1.1.2 (incremental improvements)
    • Branched: v2.0.0 (architectural changes or new training approach)

    TRAINING INTEGRATION:
    • training_config_id: Links to the training plan that produced this version
    • training_run_id: Links to the specific execution that created this artifact
    • parent_version_id: Links to previous version for lineage tracking
    • External models: These fields are null as training occurs outside our control

    EXTERNAL MODEL VERSIONING:
    For third-party models (GPT, Gemini, Claude), versions track:
    • API endpoint configurations and authentication setup
    • Structured output schemas and inference parameters  
    • Performance benchmarks and cost optimization settings
    • Fallback strategies and reliability monitoring

    LIFECYCLE STATES (version_status):
    DRAFT → TRAINING → TRAINED → VALIDATED → DEPLOYED → SERVING → RETIRED
    
    DEPLOYMENT PATTERN:
    Version artifacts remain immutable. Deployment and hosting details are managed
    by AIModelServingInstance to support:
    • Multi-region deployments (same version in multiple regions)
    • A/B testing (same version with different configurations)
    • Environment separation (staging vs production)
    • Multiple hosting patterns (persistent, ephemeral, hybrid)

    PERFORMANCE TRACKING:
    Each version tracks real-world performance to enable:
    • Comparative analysis between training frequencies/approaches
    • Performance degradation detection over time
    • ROI analysis of different training strategies
    • Cost optimization for external model usage
    • Automated rollback triggers for quality control

    ARTIFACT MANAGEMENT:
    • model_artifact_location: Physical storage of trained model (GCS, S3, etc.)
    • model_artifact_checksum: Integrity verification for deployments
    • model_artifact_format: Serialization format (pickle, ONNX, TensorFlow SavedModel)
    • artifact_size_mb: Resource planning and transfer optimization
    """

    VERSION: ClassVar[int] = 3
    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    DOMAIN: ClassVar[str] = "papp_oracle_fincore_prediction"
    OBJ_REF: ClassVar[str] = "aimodelversion"

    # --- Identifiers and Relationships ---
    model_version_id: str = Field(..., description="The unique identifier for this specific model version.")
    model_version_name: Optional[str] = Field(None, description="Human-readable version name, e.g., 'Summer_2024_Production'.")
    model_version_number: Optional[str] = Field(None, description="Semantic version number, e.g., '1' or '202408061'.")
    model_spec_id: str = Field(..., description="Reference to the AIModelSpecification this version implements.")
    training_config_id: Optional[str] = Field(None, description="Reference to the AITrainingAndUpdateConfiguration following which this model was created. I.E. the training plan. (Unknown for external models)")
    training_run_id: Optional[str] = Field(None, description="Reference to the AITrainingOrUpdateRun that produced this version (Unknown for external models).")
    parent_version_id: Optional[str] = Field(None, description="Reference to the parent model version from which this one was retrained, fine-tuned or updated.")

    # --- Model State and Status ---
    version_status: AIModelStatus = Field(..., description="Current lifecycle status of this model version.")
    pulse_status: ObjectOverallStatus = Field(default=ObjectOverallStatus.ACTIVE, description="Whether this model version is actively used: ACTIVE (in use), INACTIVE (not in use), DRAFT (being prepared), RETIRED (permanently discontinued).")
    version_overall_pulse_performance_score: Optional[float] = Field(None, description="Overall performance assessment score for this version. Used for ranking and comparison.")
   
    # --- Lifecycle Timestamps and Governance ---
    deployment_to_production_approved_by: Optional[str] = Field(None, description="Who approved this model version for deployment.")
    approval_notes: Optional[str] = Field(None, description="Notes from the approval process.")
    deployed_to_production_datetime: Optional[datetime] = Field(None, description="When this model version was first used for production inference.")
    version_retired_datetime: Optional[datetime] = Field(None, description="When this model version was retired from active use.")
    drift_detection_enabled: bool = Field(True, description="Whether drift detection is enabled for this model version.")
   
    # --- Model Artifacts ---
    model_artifact_location: Optional[str] = Field(None, description="Primary storage location of the trained model artifact.")
    model_artifact_checksum: Optional[str] = Field(None, description="Checksum/hash of the model artifact for integrity verification.")
    model_artifact_size_mb: Optional[float] = Field(None, description="Size of the model artifact in MB.")
    model_artifact_format: Optional[str] = Field(None, description="Format of the model artifact, e.g., 'pickle', 'onnx', 'tensorflow_savedmodel'.")
    
    # NOTE: Hosting and deployment information is handled by AIModelServingInstance 
    # to support multiple serving instances per model version (multi-region, A/B testing, different hosting patterns)

    # --- Metadata ---
    model_description: Optional[str] = Field(None, description="Description of what makes this model version unique.")
    release_notes: Optional[str] = Field(None, description="Release notes describing changes and improvements.")
    known_limitations: Optional[str] = Field(None, description="Known limitations or issues with this model version.")
    strengths: Optional[str] = Field(None, description="Strengths of this model version, e.g., 'high accuracy on recent data'.")
    weaknesses: Optional[str] = Field(None, description="Weaknesses of this model version (e.g., 'struggles with outliers').")
    recommended_use_cases: Optional[List[str]] = Field(None, description="Recommended use cases for this model version.")
    notes: Optional[str] = Field(None, description="Additional notes about this model version.")
    tags: Dict[str, str] = Field(default_factory=dict, description="Tags for categorization and filtering.")

    # --- Namespace and Identity ---
    pulse_namespace: Optional[str] = Field(None, description="Namespace for this AI model version.")
    namespace_id_seed_phrase: Optional[str] = Field(None, description="Seed phrase used for namespace-based UUID generation.")

    # Audit fields - created fields are frozen after creation, updated fields are mutable
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)
    created_by: Optional[str] = Field(..., frozen=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(...)

    
