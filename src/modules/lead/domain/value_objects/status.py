from enum import Enum
from dataclasses import dataclass

class StatusEnum(Enum):
    NEW = "Novo"
    UNDER_REVIEW = "Em revisão" 
    CONTACTED = "Contatado" 
    CONVERTED = "Convertido"
    LOST = "Perdido"

@dataclass
class LeadStatus:
    value: StatusEnum

    @classmethod
    def from_str(cls, value:str) -> "LeadStatus":

        mapping = {
            "NEW": StatusEnum.NEW,
            "UNDER_REVIEW": StatusEnum.UNDER_REVIEW,
            "CONTACTED": StatusEnum.CONTACTED,
            "CONVERTED": StatusEnum.CONVERTED,
            "LOST": StatusEnum.LOST,
        }

        return cls(mapping[value])

    def __str__(self) -> str:
        return self.value.value