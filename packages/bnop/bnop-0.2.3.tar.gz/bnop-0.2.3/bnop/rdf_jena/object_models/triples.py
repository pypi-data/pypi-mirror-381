from dataclasses import dataclass


@dataclass
class Triple:
    """Representation of an RDF triple."""

    subject: str
    predicate: str
    object: str

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        if not self.subject:
            raise ValueError("subject required")
        if not self.predicate:
            raise ValueError("predicate required")
        if not self.object:
            raise ValueError("object required")

    def to_n_triple(self) -> str:
        self.validate()
        return f"{self.subject} {self.predicate} {self.object} ."
