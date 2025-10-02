from dataclasses import dataclass
from typing import ClassVar

from bclearer_core.configurations.b_clearer_configurations.b_clearer_configurations import (
    BClearerConfigurations,
)


@dataclass
class JenaConfigurations(BClearerConfigurations):
    """Settings for connecting to Jena stores."""

    jena_store_type: str
    jena_store_path: str
    enable_reasoning: bool = False
    reasoner_type: str = "OWL_DL"

    VALID_STORE_TYPES: ClassVar[set[str]] = {"TDB2", "IN_MEMORY"}

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if self.jena_store_type not in self.VALID_STORE_TYPES:
            raise ValueError(
                "jena_store_type must be 'TDB2' or 'IN_MEMORY'",
            )
        if self.jena_store_type == "TDB2" and not self.jena_store_path:
            raise ValueError("jena_store_path required for TDB2 store")
        if self.jena_store_type == "IN_MEMORY":
            self.jena_store_path = ""

    @classmethod
    def create_tdb2(
        cls,
        store_path: str,
        enable_reasoning: bool = False,
        reasoner_type: str = "OWL_DL",
    ) -> "JenaConfigurations":
        return cls(
            jena_store_type="TDB2",
            jena_store_path=store_path,
            enable_reasoning=enable_reasoning,
            reasoner_type=reasoner_type,
        )

    @classmethod
    def create_in_memory(
        cls,
        enable_reasoning: bool = False,
        reasoner_type: str = "OWL_DL",
    ) -> "JenaConfigurations":
        return cls(
            jena_store_type="IN_MEMORY",
            jena_store_path="",
            enable_reasoning=enable_reasoning,
            reasoner_type=reasoner_type,
        )
