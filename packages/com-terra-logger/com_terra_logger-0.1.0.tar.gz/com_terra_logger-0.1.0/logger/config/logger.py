import logging
from dataclasses import dataclass, field
from typing import Optional

from .format import LoggerFormatConfig

@dataclass
class LoggerConfig:
    """
    Defines the configuration for logger initialization.
    """
    level: str = "DEBUG"
    fmt: LoggerFormatConfig = field(default_factory=LoggerFormatConfig)
    file_path: Optional[str] = None # Optional file output
    propagate: Optional[bool] = False  # Avoid duplication in FastAPI
    structured: Optional[bool] = False

    def get_level(self) -> int:
        """Convert level string to logging constant."""
        return getattr(logging, self.level.upper(), logging.INFO)
