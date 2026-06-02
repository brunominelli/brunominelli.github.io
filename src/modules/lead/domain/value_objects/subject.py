from enum import Enum

class SubjectEnum(Enum):
    REPORT_AND_DATA = "report_and_data" 
    OPERATIONAL_PROCESS = "operational_process" 
    API = "api" 

    @property
    def label(self) -> str:

        labels = {
            SubjectEnum.REPORT_AND_DATA: "Automação de relatórios e dados",
            SubjectEnum.OPERATIONAL_PROCESS: "Fluxos e Processos Operacionais",
            SubjectEnum.API: "Integrações e APIS",
        }

        return labels[self]
