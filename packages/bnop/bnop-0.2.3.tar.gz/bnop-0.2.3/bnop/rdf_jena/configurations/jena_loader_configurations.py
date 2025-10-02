from dataclasses import dataclass

from bclearer_core.configurations.b_clearer_configurations.b_clearer_configurations import (
    BClearerConfigurations,
)


@dataclass
class JenaLoaderConfigurations(BClearerConfigurations):
    """Settings for bulk loading to Jena."""

    batch_size: int = 1000
    parallel_workers: int = 4
    streaming_threshold_mb: int = 100
    cache_size_mb: int = 500
    use_bulk_loader: bool = True

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if self.batch_size <= 0:
            raise ValueError("batch_size must be positive")
        if self.parallel_workers <= 0:
            raise ValueError(
                "parallel_workers must be positive",
            )
        if self.streaming_threshold_mb < 0:
            raise ValueError(
                "streaming_threshold_mb must be non-negative",
            )
        if self.cache_size_mb <= 0:
            raise ValueError("cache_size_mb must be positive")
