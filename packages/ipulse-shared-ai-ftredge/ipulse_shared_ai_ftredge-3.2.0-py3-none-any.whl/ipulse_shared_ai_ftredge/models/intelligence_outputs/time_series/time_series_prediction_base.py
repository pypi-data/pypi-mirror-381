"""Common base model for all time series predictions (LLM and Quant)."""
from typing import ClassVar, Dict, Any, Literal, Optional, Union, List
from datetime import datetime, timezone
from pydantic import Field, BaseModel
from ipulse_shared_base_ftredge.enums import (ModelOutputPurpose, ProgressStatus, TimeFrame)

class TimeSeriesPredictionValuesBase(BaseModel):
    """Separate class for actual prediction values that reference a prediction log."""

    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    VERSION: ClassVar[int] = 2
    DOMAIN: ClassVar[str] = "dp_oracle_prediction"
    OBJ_REF: ClassVar[str] = "tspredvalues"
    
    # --- Core Identity ---
    prediction_values_id: Optional[str] = Field(None, description="Optional unique identifier for this set of prediction values - not needed when using prediction_log_id + timestamp")
    prediction_log_id: str = Field(..., description="Reference to the TimeSeriesPredictionLog that generated these values")
    
    # --- Value Point Structure ---
    prediction_timestamp_utc: Union[datetime, str] = Field(..., description="Timestamp of the prediction in datetime utc format or YYYY-MM-DD format")
    prediction_value: float = Field(..., description="Predicted value")
    prediction_value_upper_bound: Optional[float] = Field(None, description="Upper bound of the prediction confidence interval")
    prediction_value_lower_bound: Optional[float] = Field(None, description="Lower bound of the prediction confidence interval")
    prediction_confidence_score: Optional[float] = Field(None, description="Confidence score of the prediction")
    
    # --- Time Series Components (for quant models) ---
    trend_component: Optional[float] = Field(None, description="Trend component for this prediction point")
    seasonal_component: Optional[float] = Field(None, description="Seasonal component for this prediction point")
    residual_component: Optional[float] = Field(None, description="Residual component for this prediction point")
    
     # --- Quality Indicators ---
    is_anomaly: Optional[bool] = Field(None, description="Whether this prediction point is flagged as anomalous")
    uncertainty_score: Optional[float] = Field(None, description="Uncertainty score for this prediction point")

    # --- Metadata ---
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata for this prediction value")

class TimeSeriesPredictionLog(BaseModel):
    """
    Common base class for all time series predictions.
    Contains fields that apply to ANY time series prediction, regardless of method (LLM or Quant).
    """
    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    VERSION: ClassVar[int] = 2
    DOMAIN: ClassVar[str] = "dp_oracle_prediction"
    OBJ_REF: ClassVar[str] = "tspredlog"
    
    # --- Core Identity ---
    prediction_log_id: str = Field(..., description="Unique identifier for this prediction")
    prediction_purpose: ModelOutputPurpose = Field(..., description="Training, Validation, Serving..")
    
    # --- Target Context ---
    target_subject_id: str = Field(..., description="ID of the subject being predicted")
    predicted_records_type: Optional[str] = Field(None, description="Type of records being predicted, e.g., 'eod_adjc', 'intraday_adjc', 'eod_sentiment_score' etc")
    target_subject_name: str = Field(..., description="Name of the subject being predicted")
    target_subject_description: Optional[Dict[str, Any]] = Field(None, description="eg.: {'sector_records_category': 'MARKET', 'subject_category': 'EQUITY', 'contract_type': 'SPOT'} ")
   
    # --- AI Model Context ---
    model_specification_id: str = Field(..., description="ID of the AI model specification")
    model_name: str = Field(..., description="Readable Name of the AI model")
    model_version_id: str = Field(..., description="Version of the AI model. For internal model this comes from AIModelVersion")
    model_version_name: Optional[str] = Field(None, description="Human-readable version name, e.g., 'Summer_2024_Production'.")
    model_features_used: Optional[Dict[str, Any]] = Field(None, description="Features used from the model, e.g., {'deep_thinking': True, 'function_calling': False}")
    # --- Model Serving Context (Optional - for MLOps tracking) ---
    model_serving_instance_id: Optional[str] = Field(None, description="ID of the specific serving instance used for this prediction")
    model_serving_instance_name: Optional[str] = Field(None, description="Name of the serving instance used for this prediction")

    # Input sources with strong typing
    input_structure: List[Dict[str, Any]] = Field(default_factory=list, description="Strongly typed input sources used for this prediction")
    # Example structure:
    # [
    #   {
    #     "input_type": "AIIOFormat",
    #     "io_format_id": "equity_ohlcv_daily_v1",
    #     "source_location": "bigquery://project.dataset.table",
    #     "rows_count": 252,
    #     "feature_store_version": "v1.2.3",
    #     "temporal_range_start": "2024-01-15",
    #     "temporal_range_end": "2024-12-31",
    #     "feature_columns_used": ["open_normalized", "volume_log"],
    #     "preprocessing_applied": {"outlier_removal": True}
    #   },
    #   {
    #     "input_type": "AIIOFormat", 
    #     "io_format_id": "financial_prompt_v1",
    #     "prompt_text": "Analyze AAPL stock performance...",
    #   }
    # ]
    
    # Traditional output schema reference (for fixed models)

    output_structure: Optional[Dict[str, Any]] = Field(None, description="Strongly typed output data schema used for this prediction")
    # Example structure:
    # {
    #   "output_type": "AIIOFormat",
    #   "io_format_id": "equity_price_forecast_v1",

    # --- Value Context Summary (not the actual values) ---
    prediction_values_start_timestamp_utc: Optional[Union[datetime, str]] = Field(None, description="Start of prediction horizon")
    prediction_values_end_timestamp_utc: Optional[Union[datetime, str]] = Field(None, description="End of prediction horizon")
    prediction_steps_count: int = Field(..., description="Number of time steps predicted.")
    prediction_step_timeframe: TimeFrame = Field(..., description="Time frequency of predictions.")
    
    # --- Prediction Status ---
    prediction_status: ProgressStatus = Field(..., description="Status of the prediction generation process.")
    retry_attempts: Optional[int] = Field(None, description="Number of retry attempts made (LLM predictions only)")
    prediction_error: Optional[str] = Field(None, description="Error message if prediction failed")

    # --- Prediction Execution Context ---
    prediction_approach: Literal["single", "batch"] = Field(..., description="Method used to generate this prediction")
    prediction_requested_datetime_utc: datetime = Field(..., description="When prediction was requested")
    prediction_received_datetime_utc: datetime = Field(..., description="When response was received")
    prediction_cost_usd: Optional[float] = Field(None, description="Cost of prediction in USD")

    # --- Method-Specific Fields (LLM) ---
    # prompt_variant_id: Optional[str] = Field(None, description="ID of the prompt variant used (LLM predictions only)")
    input_tokens_count: Optional[int] = Field(None, description="Number of input tokens (LLM predictions only)")
    thinking_tokens_count: Optional[int] = Field(None, description="Number of thinking/reasoning tokens (LLM predictions only)")
    output_tokens_count: Optional[int] = Field(None, description="Number of output tokens (LLM predictions only)")
    total_output_tokens_billed: Optional[int] = Field(None, description="Total output tokens billed (LLM predictions only)")
    finish_reason: Optional[str] = Field(None, description="Reason the prediction completed (LLM predictions only)")
    reasoning_trace: Optional[str] = Field(None, description="LLM reasoning trace if available (LLM predictions only)")
    raw_response: Optional[Dict[str, Any]] = Field(None, description="Raw response from LLM (LLM predictions only)")
    
    # --- Metadata ---
    tags: Optional[str] = Field(None, description="Comma-separated tags for categorization and filtering")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")

    # Audit fields - created fields are frozen after creation, updated fields are mutable
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)
    created_by: Optional[str] = Field(..., frozen=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(...)

    class Config:
        extra = "forbid"  # Prevent unexpected fields
