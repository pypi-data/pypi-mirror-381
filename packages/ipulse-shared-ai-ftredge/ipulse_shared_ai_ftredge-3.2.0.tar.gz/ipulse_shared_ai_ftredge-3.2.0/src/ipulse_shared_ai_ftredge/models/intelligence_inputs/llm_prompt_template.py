from typing import List, Optional, Dict, Any, Literal, ClassVar
from datetime import datetime, timezone
from pydantic import Field, BaseModel
from ipulse_shared_base_ftredge import (DataModality,
                                        DataStructureLevel,
                                        ModalityContentDynamics,
                                        ObjectOverallStatus)


class AIPromptTemplate(BaseModel):
    """
    AI Prompt Template definitions for language models.
    
    This class manages prompt templates that can be used with AI models,
    particularly for LLM applications. Templates are linked to models and 
    subjects through the xref_subject_aimodel_ioformats table.
    
    Supports flexible content storage strategies:
    - Inline: Template content stored directly in this record
    - File reference: Template stored in external file (GCS, local filesystem)
    - Schema query: Template dynamically generated from schema/database queries
    """

    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] =""
    VERSION: ClassVar[int] = 1
    DOMAIN: ClassVar[str] = "dp_oracle_fincore_prediction"
    OBJ_REF: ClassVar[str] = "aiprompttemplate"
    
    # Core identification
    prompt_template_id: str = Field(
        ..., 
        description="Unique identifier for this prompt template"
    )
    
    template_name: str = Field(
        ..., 
        description="Human-readable name for this template, e.g., 'Financial_Analysis_Chain_of_Thought'"
    )
    
    template_version: str = Field(
        ..., 
        description="Version of this template (semantic versioning recommended)"
    )
    
    template_type: Literal["system", "user", "assistant", "function", "composite"] = Field(
        ..., 
        description="Type of prompt: system (instructions), user (query), assistant (example), function (tool), composite (multiple parts)"
    )
    
    # Content storage strategy
    content_storage_type: Literal["inline", "file_reference", "schema_query"] = Field(
        ..., 
        description="How template content is stored: inline (in this record), file_reference (external file), schema_query (dynamic generation)"
    )
    
    # Inline content (when content_storage_type = "inline")
    template_content: Optional[str] = Field(
        None, 
        description="The actual prompt template content (use when content_storage_type='inline')"
    )
    
    # File reference content (when content_storage_type = "file_reference")
    file_path: Optional[str] = Field(
        None, 
        description="Path to external file containing template content (GCS path, local path, etc.)"
    )
    
    file_format: Optional[Literal["txt", "json", "yaml", "md", "jinja2"]] = Field(
        None, 
        description="Format of the external file"
    )
    
    # Schema query content (when content_storage_type = "schema_query")
    query_template: Optional[str] = Field(
        None, 
        description="SQL or other query template to dynamically generate prompt content"
    )
    
    query_parameters: Optional[Dict[str, Any]] = Field(
        default_factory=dict, 
        description="Parameters for the query template"
    )
    
    # Template metadata
    variable_placeholders: Optional[List[str]] = Field(
        default_factory=list, 
        description="List of variable names that can be substituted in the template, e.g., ['subject_name', 'analysis_date', 'market_data']"
    )
    
    template_engine: Optional[Literal["jinja2", "f_string", "simple_replacement", "mustache"]] = Field(
        default="simple_replacement", 
        description="Template engine to use for variable substitution"
    )
    
    # Context and constraints
    max_tokens: Optional[int] = Field(
        None, 
        description="Maximum number of tokens this template should produce"
    )
    
    expected_response_format: Optional[str] = Field(
        None, 
        description="Expected format of model response: 'json', 'text', 'markdown', etc."
    )
    
    temperature_suggestion: Optional[float] = Field(
        None, 
        description="Suggested temperature setting for this template (0.0-2.0)"
    )
    
    # Validation and testing
    example_variables: Optional[Dict[str, Any]] = Field(
        default_factory=dict, 
        description="Example values for template variables (used for testing and validation)"
    )
    
    example_output: Optional[str] = Field(
        None, 
        description="Example of expected model output when using this template"
    )
    
    validation_schema: Optional[Dict[str, Any]] = Field(
        default_factory=dict, 
        description="JSON schema for validating the model's response format"
    )
    
    # Relationships and compatibility
    compatible_model_types: Optional[List[str]] = Field(
        default_factory=list, 
        description="List of AI model types this template works with, e.g., ['gpt-4', 'claude-3', 'llama-2']"
    )
    
    required_model_capabilities: Optional[List[str]] = Field(
        default_factory=list, 
        description="Required model capabilities, e.g., ['function_calling', 'json_mode', 'vision']"
    )
    
    # Hierarchical templates (for composite templates)
    parent_template_id: Optional[str] = Field(
        None, 
        description="Reference to parent template if this is a component of a larger template system"
    )
    
    child_template_ids: Optional[List[str]] = Field(
        default_factory=list, 
        description="List of child template IDs for composite templates"
    )
    
    template_execution_order: Optional[int] = Field(
        None, 
        description="Execution order for child templates in composite systems"
    )
    
    # Usage tracking and optimization
    usage_context: Optional[str] = Field(
        None, 
        description="Context where this template is typically used, e.g., 'financial_analysis', 'data_summarization'"
    )
    
    performance_notes: Optional[str] = Field(
        None, 
        description="Notes about template performance, common issues, optimization tips"
    )
    
    tags: Optional[List[str]] = Field(
        default_factory=list, 
        description="Tags for categorization and discovery"
    )
    
    # Audit fields - created fields are frozen after creation, updated fields are mutable
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)
    created_by: Optional[str] = Field(..., frozen=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(...)

    # Standard metadata fields inherited from BaseNoSQLModel
    # pulse_status, created_at, updated_at, created_by, updated_by, etc.
    
    class Config:
        """Pydantic model configuration"""
        schema_extra = {
            "example": {
                "prompt_template_id": "financial_analysis_cot_v1",
                "template_name": "Financial Analysis Chain of Thought",
                "template_version": "1.0.0",
                "template_type": "user",
                "content_storage_type": "inline",
                "template_content": """You are a financial analyst. Analyze the following market data for {subject_name} and provide insights.

Market Data:
{market_data}

Please provide your analysis using the following structure:
1. Key Observations
2. Trends Analysis  
3. Risk Assessment
4. Recommendations

Use chain-of-thought reasoning and show your work.""",
                "variable_placeholders": ["subject_name", "market_data"],
                "template_engine": "simple_replacement",
                "max_tokens": 2000,
                "expected_response_format": "markdown",
                "temperature_suggestion": 0.3,
                "compatible_model_types": ["gpt-4", "claude-3", "gemini-pro"],
                "usage_context": "financial_analysis",
                "tags": ["finance", "analysis", "chain-of-thought"]
            }
        }
