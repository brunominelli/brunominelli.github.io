from src.modules.lead.domain.value_objects.status import StatusEnum
from src.modules.lead.application.dtos.lead_kpis_dto import LeadKpisDTO
from src.modules.lead.domain.repositories.i_lead_repository import ILeadRepository

class ReadKpisUseCase:
    def __init__(self, repository:ILeadRepository):
        self.repository = repository

    def execute(self) -> LeadKpisDTO:
        leads = self.repository.read_all()

        new = 0
        under_review = 0
        contacted = 0
        converted = 0
        lost = 0

        for lead in leads:
            if lead.status == StatusEnum.NEW.value:
                new += 1
            elif lead.status == StatusEnum.UNDER_REVIEW.value:
                under_review += 1
            elif lead.status == StatusEnum.CONTACTED.value:
                contacted += 1
            elif lead.status == StatusEnum.CONVERTED.value:
                converted += 1
            elif lead.status == StatusEnum.LOST.value:
                lost += 1

        return LeadKpisDTO(
            all=len(leads),
            new=new,
            under_review=under_review,
            contacted=contacted,
            converted=converted,
            lost=lost
        )