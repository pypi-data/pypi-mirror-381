from typing import List, Optional, Literal, ClassVar
from pydantic import Field, BaseModel
from datetime import datetime, timezone
from ipulse_shared_base_ftredge import (DataModality,
                                        DataStructureLevel,
                                        ModalityContentDynamics,
                                        ObjectOverallStatus,
                                        DataResource,
                                        SectorRecordsCategory)

class AIIOFormat(BaseModel):
    """
    🎯 AI INPUT/OUTPUT FORMAT - Structured Data Interface Specification

    CORE CONCEPT:
    Defines standardized format specifications for AI model inputs and outputs, supporting both
    simple standalone formats and complex hierarchical compositions. This registry-based approach
    enables flexible pipeline orchestration by separating format definitions from model implementations.

    HIERARCHICAL ARCHITECTURE:
    • Standalone: Independent format (e.g., 'CSV_TimeSeries_OHLCV')
    • Parent: Composite format combining multiple children (e.g., 'text_prompt + excel_file + image')
    • Child: Component format used within parent compositions

    MULTIMODAL SUPPORT:
    Comprehensive support for diverse data types through structured enums:
    • Data Modalities: TEXT, TABULAR, IMAGE, AUDIO, VIDEO, JSON_TEXT, etc.
    • Structure Levels: STRUCTURED, SEMI_STRUCTURED, UNSTRUCTURED  
    • Content Dynamics: STATIC, SEQUENCE, TIMESERIES, STREAMING
    • Resource Formats: in_memory_data, file_json, file_csv, file_png, api_endpoint, etc.

    LINKING STRATEGY:
    Format-to-model relationships are managed through external cross-reference tables
    (xref_subject_aimodel_ioformats), following established architectural patterns for
    scalable pipeline orchestration and avoiding tight coupling.

    DATA SOURCE INTEGRATION:
    • Schema References: Links to existing data schemas with version constraints
    • Resource Locations: GCS buckets, S3 paths, API endpoints, local directories
    • SQL Transformations: Optional queries for data extraction/transformation
    • Subject Targeting: Single-subject, multi-subject, or non-subject data patterns

    FORMAT-SPECIFIC CONFIGURATIONS:
    • Tabular: Index columns, target variables, data type mappings, row constraints
    • Text: Language, templates, length limits, allowed formats (markdown, plain, HTML)
    • JSON: Schema definitions, required/optional fields, nesting depth limits
    • Image: Format, dimensions, color channels, quality settings
    • Audio: Format, sample rates, channel configurations (future extensibility)

    EXAMPLE USE CASES:
    • Input: 'Financial_TimeSeries_OHLCV_Daily' → tabular format with date index, OHLCV columns
    • Output: 'Prediction_JSON_Classification' → structured JSON with probabilities and metadata  
    • Composite: 'Prompt_Plus_Spreadsheet' → parent format combining text prompt + Excel file children
    """

    VERSION: ClassVar[int] = 3
    SCHEMA_ID: ClassVar[str] = ""
    SCHEMA_NAME: ClassVar[str] = ""
    DOMAIN: ClassVar[str] = "dp_oracle_fincore_prediction"
    OBJ_REF: ClassVar[str] = "aiioformat"

    # Core identification
    io_format_id: str = Field(..., description="Unique identifier for this I/O format")
    io_format_name: str = Field(..., description="Human-readable name, e.g., 'Financial_TimeSeries_OHLCV'")
    io_format_version: str = Field(..., description="Version of this I/O format (e.g., '1.0', '2.1.0')")
    io_type: Literal["input", "output"] = Field(..., description="Whether this is input or output format")
    pulse_status: ObjectOverallStatus = Field(default=ObjectOverallStatus.ACTIVE, description="Status of this I/O format")
    
    # Parent/Child IO Format Support
    parent_io_format_id: Optional[str] = Field(None, description="Reference to parent IO format for composite formats (e.g., 'text_prompt + excel_file')")
    child_io_format_ids: Optional[str] = Field(None, description="Comma-separated child IO format IDs for composite parent formats")
    io_format_hierarchy_level: Literal["standalone", "parent", "child"] = Field(default="standalone", description="Whether this is a standalone, parent (composite), or child format")
    
    # Schema reference (parent schema this format may inherit from)
    data_schema_id: Optional[str] = Field(None, description="Reference to the schema from where data is coming or to where it's going. But doesn't mean it's the exact schema of this io format, can be a subset.")
    data_schema_version_constraint: Optional[str] = Field(None, description="Version constraint: '>3.0 <4.0', 'latest', 'compatible with 3.0'")
    resource_location: Optional[str] = Field(None, description="Location of the resource, especially if no schema referenced eg //gcs/bucket/folder or s3://bucket/folder or local path /data/folder")
    api_url: Optional[str] = Field(None, description="API endpoint URL if applicable")
    sql_query: Optional[str] = Field(None, description="Optional SQL query to extract/transform data from the parent schema")
    
    # Data characteristics
    data_modality: DataModality = Field(..., description="Primary data modality: TEXT, TABULAR, IMAGE, etc.")
    data_structure_level: DataStructureLevel = Field(..., description="Structure level: STRUCTURED, SEMI_STRUCTURED, UNSTRUCTURED")
    content_dynamics: List[ModalityContentDynamics] = Field(..., description="Content dynamics: STATIC, SEQUENCE, TIMESERIES, etc.")
    resource_format: Optional[DataResource] = Field(default_factory=list, description="Specific resource/data content formats, e.g., ['in_memory_data', 'file_json', 'file_png']")
    encoding: Optional[str] = Field(None, description="Character encoding, e.g., 'utf-8', 'ascii'")
    compression: Optional[str] = Field(None, description="Compression format: 'gzip', 'lz4', 'none'")
    data_characteristics_notes: Optional[str] = Field(None, description="Additional notes on data characteristics")
    # Subject definition
    subjects_generalization_support: Literal["single_subject", "multi_subject", "non_subject"] = Field(..., description="How this format relates to subjects")
    subjects_selection_criteria: Optional[str] = Field(None, description="Criteria for multi-subject formats selection, e.g., 'subject_category=equity AND subject_category_detailed=stock AND contract_type=spot'")

    # Tabular/JSON-specific fields (populated only for TABULAR and sometimes JSON modalities)
    index_columns: Optional[str] = Field(None, description="Comma-separated index column names, e.g., 'date,ticker'")
    target_variable_names: Optional[str] = Field(None, description="Comma-separated target variable names")
    auxiliary_variable_names: Optional[str] = Field(None, description="Comma-separated auxiliary variable names")
    data_types_mapping: Optional[str] = Field(None, description="JSON string of column data types mapping")
    row_count_min: Optional[int] = Field(None, description="Minimum expected number of rows")
    row_count_max: Optional[int] = Field(None, description="Maximum expected number of rows")
    
    # Text-specific fields (populated only for TEXT modality)
    text_type: Optional[str] = Field(None, description="Type of text: 'prompt_template', 'response', 'document'")
    max_length_chars: Optional[int] = Field(None, description="Maximum text length in characters")
    min_length_chars: Optional[int] = Field(None, description="Minimum text length in characters")
    language: Optional[str] = Field(None, description="Primary language: 'english', 'multilingual'")
    template_variables: Optional[str] = Field(None, description="Comma-separated template variable names")
    allowed_formats: Optional[str] = Field(None, description="Comma-separated allowed text formats: 'markdown', 'plain', 'html'")
    
    # JSON-specific fields (populated only for JSON_TEXT modality)
    json_schema_definition: Optional[str] = Field(None, description="JSON Schema definition as string")
    required_fields: Optional[str] = Field(None, description="Comma-separated required field names")
    optional_fields: Optional[str] = Field(None, description="Comma-separated optional field names")
    max_nesting_depth: Optional[int] = Field(None, description="Maximum allowed JSON nesting depth")
    
    # Image-specific fields (populated only for IMAGE modality)
    image_format: Optional[str] = Field(None, description="Image format: 'PNG', 'JPEG', 'GIF', 'WEBP'")
    image_width: Optional[int] = Field(None, description="Image width in pixels")
    image_height: Optional[int] = Field(None, description="Image height in pixels")
    image_channels: Optional[int] = Field(None, description="Number of color channels: 1 (grayscale), 3 (RGB), 4 (RGBA)")
    color_space: Optional[str] = Field(None, description="Color space: 'RGB', 'CMYK', 'GRAYSCALE'")
    image_quality: Optional[int] = Field(None, description="Image quality (1-100 for JPEG)")
    
    # Audio-specific fields (for future use)
    audio_format: Optional[str] = Field(None, description="Audio format: 'WAV', 'MP3', 'FLAC'")
    sample_rate: Optional[int] = Field(None, description="Audio sample rate in Hz")
    audio_channels: Optional[int] = Field(None, description="Number of audio channels")
    
    # General metadata
    description: Optional[str] = Field(None, description="Detailed description of this I/O format")
    examples: Optional[str] = Field(None, description="JSON string of example data instances")
    validation_rules: Optional[str] = Field(None, description="JSON string of additional validation rules")

    # --- Namespace and Identity ---
    pulse_namespace: Optional[str] = Field(None, description="Namespace for this AI I/O format.")
    namespace_id_seed_phrase: Optional[str] = Field(None, description="Seed phrase used for namespace-based UUID generation.")

    # Audit fields - created fields are frozen after creation, updated fields are mutable
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)
    created_by: Optional[str] = Field(..., frozen=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(...)
    
    class Config:
        extra = "forbid"

class AIModelIOCapabilities(BaseModel):
    """Defines what I/O formats and capabilities a model supports."""
    
    # Registry format references
    io_format_ids: Optional[List[str]] = Field(default_factory=list, description="List of specific AIIOFormat IDs from registry. Leave blank if highly generalized")
    io_format_version_constraints: Optional[str] = Field(default=None, description="Version constraints for formats, e.g., '>=1.0 <2.0 or 'latest'")

    # Modality support
    modalities: List[DataModality] = Field(default_factory=list, description="Supported data modalities")
    structure_levels: List[DataStructureLevel] = Field(default_factory=list, description="Supported structure levels")
    content_dynamics: List[ModalityContentDynamics] = Field(default_factory=list, description="Supported content dynamics")
    resource_formats: Optional[List[DataResource]] = Field(default_factory=list, description="Specific resource/data content formats supported, e.g., ['in_memory_data', 'file_json', 'file_png']")
    sector_records_categories: Optional[List[SectorRecordsCategory]] = Field(default_factory=list, description="Specific sector/record categories supported, e.g., ['market', 'indicator', 'fundamental', 'knowledge' etc.]")
    # Capacity limits
    max_total_size_mb: Optional[float] = Field(None, description="Maximum total size in MB for all inputs/outputs")
    max_modalities: Optional[int] = Field(None, description="Maximum different modalities supported in single request/response")
    max_tokens: Optional[int] = Field(None, description="Maximum total tokens for text-based inputs/outputs")
    max_files: Optional[int] = Field(None, description="Maximum number of files supported in single request/response")
    notes: Optional[str] = Field(None, description="Additional notes or considerations")

    # Audit fields - created fields are frozen after creation, updated fields are mutable
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), frozen=True)
    created_by: Optional[str] = Field(..., frozen=True)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(...)