from enum import Enum

class StatusEnum(Enum):
    NEW = "new"
    UNDER_REVIEW = "under_review" 
    CONTACTED = "contacted" 
    CONVERTED = "converted" 
    LOST = "lost" 

    @property
    def label(self) -> str:

        labels = {
            StatusEnum.NEW: "Novo",
            StatusEnum.UNDER_REVIEW: "Em revisão" ,
            StatusEnum.CONTACTED: "Contatado" ,
            StatusEnum.CONVERTED: "Convertido",
            StatusEnum.LOST: "Perdido",
        }

        return labels[self]
