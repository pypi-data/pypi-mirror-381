from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class ChunkMetadata(BaseModel):
    class Config:
        # Always exclude None values and unset fields at the model level
        exclude_none = True
        exclude_unset = True

    def model_dump(self, **kwargs):
        """Override to exclude empty lists for vector store efficiency."""
        # The Config already handles exclude_none, but ensure it's enforced
        kwargs.setdefault('exclude_none', True)
        kwargs.setdefault('exclude_unset', True)
        data = super().model_dump(**kwargs)
        # Remove empty lists to save vector store space
        return {k: v for k, v in data.items() 
                if not (isinstance(v, list) and len(v) == 0)}

    # MANDATORY FIELDS FIRST (no defaults)
    language: str  # Now mandatory!
    chunk_type: str  # Also mandatory
    repo_url: str

    # OPTIONAL FIELDS 
    # File context
    file_path: Optional[str] = None
    file_name: Optional[str] = None

    # Code structure
    class_name: Optional[str] = None
    method_name: Optional[str] = None
    signature: Optional[str] = None
    return_type: Optional[str] = None
    fields: List[str] = Field(default_factory=list)
    methods: List[str] = Field(default_factory=list)

    # Chunk info
    chunk_size: int = 0
    start_line: int = 0
    end_line: int = 0

    # Processing info
    processed_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    # Fields to support openapi and readme generations
    annotations: List[str] = Field(default_factory=list)  # Method or class annotations
    class_annotations: List[str] = Field(default_factory=list)  # Class-level annotations for method chunks
    framework_type: Optional[str] = None
    is_rest_controller: bool = False
    http_methods: List[str] = Field(default_factory=list)  # For class-level: all methods in class
    api_path: Optional[str] = None

    # Enhanced RAG fields for better code understanding
    dependencies: List[str] = Field(default_factory=list)  # Classes this code uses (UserService, PaymentService, BillingClient)
    method_calls: List[str] = Field(default_factory=list)  # Methods this code calls (userService.validate, paymentService.charge)
    parent_chunk_id: Optional[str] = None  # Class hierarchy (class:MusicController for method chunks)
    operation_type: Optional[str] = None  # CRUD, AUTH, SEARCH, VALIDATION, PROCESSING
    business_flow: Optional[str] = None  # checkout, payment, user_registration, song_upload