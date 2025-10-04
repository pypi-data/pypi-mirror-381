from dataclasses import dataclass

@dataclass
class LoggerFormatConfig:
    """
    Controls which fields appear in the log format.

    Example:
        LoggerFormatConfig(time=True, level=True, name=True)
    """
    time: bool = True
    level: bool = True
    name: bool = True
    message: bool = True

    def build_format(self) -> str:
        """Dynamically construct log format string."""
        parts = []

        if self.time:
            parts.append("%(asctime)s")

        if self.level:
            parts.append("[%(levelname)s]")

        if self.name:
            parts.append("%(name)s:")

        if self.message:
            parts.append("%(message)s")

        return " ".join(parts)
