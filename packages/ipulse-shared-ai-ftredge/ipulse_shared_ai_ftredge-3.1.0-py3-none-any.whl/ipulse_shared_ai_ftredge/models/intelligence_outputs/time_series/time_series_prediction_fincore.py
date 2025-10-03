"""Market asset investment rating and analysis (LLM output)."""
from typing import ClassVar, Optional
from pydantic import Field, BaseModel
from datetime import datetime, timezone
from ipulse_shared_base_ftredge.enums import AssetRating
from ..utils.fincore_key_risks import (
    MarketKeyRisks
)
from .time_series_prediction_base import TimeSeriesPredictionValuesBase

class TimeSeriesPredictionValuesFincore(TimeSeriesPredictionValuesBase):
    """
    Extended prediction values class to include market asset-specific fields.
    Inherits from TimeSeriesPredictionValues and adds market-specific analysis fields.
    """
    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    VERSION: ClassVar[int] = 1
    DOMAIN: ClassVar[str] = "dp_oracle_fincore_prediction"
    OBJ_REF: ClassVar[str] = "tspredvaluesfincore"

    # --- Market-Specific Analysis (for Opinionated market predictions i.e. LLMs, Experts, Public etc.) ---
    key_milestones_and_events: Optional[str] = Field(None, description="Key milestones and events affecting this prediction point")
    most_influencing_technical_factors: Optional[str] = Field(None, description="Technical analysis factors")
    most_influencing_fundamental_factors: Optional[str] = Field(None, description="Fundamental analysis factors")

class FincorePredictionInvestmentRating(BaseModel):
    """
    Investment rating and qualitative analysis for market assets.
    This is one of the outputs produced by LLM market predictions (alongside prediction values).
    References the prediction log that generated this analysis.
    """
    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    VERSION: ClassVar[int] = 1
    DOMAIN: ClassVar[str] = "dp_oracle_fincore_prediction"
    OBJ_REF: ClassVar[str] = "marketrating"
    
    # --- Core Identity ---
    investment_rating_id: str = Field(..., description="Unique identifier for this investment rating")
    prediction_log_id: str = Field(..., description="Reference to the TimeSeriesPredictionLog that generated this analysis")
    target_subject_id: str = Field(..., description="ID of the asset being analyzed (e.g., 'AAPL', 'BTC')")
    target_subject_symbol: str = Field(..., description="Symbol of the asset being analyzed (e.g., 'AAPL', 'BTC')")
    analysis_timestamp_utc: datetime = Field(..., description="When this analysis was generated")
    
    # --- Investment Analysis ---
    key_prediction_assumptions: Optional[str] = Field(None, description="Key assumptions underlying the analysis")
    overall_rating: Optional[AssetRating] = Field(None, description="Overall analyst rating for the asset (BUY, HOLD, SELL)")
    investment_thesis: Optional[str] = Field(None, description="Investment thesis provided by the LLM")
    
    # --- Risk Analysis ---
    key_risks: Optional[MarketKeyRisks] = Field(None, description="Asset-specific risk analysis based on asset type")
    volatility_assessment: Optional[str] = Field(None, description="Volatility analysis and expectations")
    
    # --- Supporting Analysis ---
    macroeconomic_supportive_conditions_analysis: Optional[str] = Field(None, description="Analysis of current macroeconomic conditions affecting the asset.")
    market_conditions_analysis: Optional[str] = Field(None, description="Analysis of current market conditions affecting the asset.")
    sector_conditions_analysis: Optional[str] = Field(None, description="Sector-specific analysis and trends.")
    competitive_positioning_analysis: Optional[str] = Field(None, description="Competitive positioning analysis.")

    # --- Recommendations ---
    time_horizon_days: Optional[int] = Field(None, description="Recommended investment time horizon (in days)")
    
    # --- Metadata ---
    confidence_in_analysis: Optional[float] = Field(None, description="LLM's or Expert's subjective confidence in this analysis (0-1)")
    analysis_metadata: Optional[dict] = Field(default_factory=dict, description="Additional analysis metadata")
