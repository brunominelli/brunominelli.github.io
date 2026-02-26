import uuid
from datetime import date, timedelta

from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.entities.offer import Offer
from src.modules.institutional.domain.repositories.i_offer_repository import IOfferRepository

class GenerateOfferUseCase:
    def __init__(self, repository:IOfferRepository):
        self.repository = repository
    
    def execute(self, lead:Lead) -> dict:
        implantation_value = 0.0
        maintence_value = 0.0

        if lead.sheet_amount.value == '1 planilha':
            implantation_value = 750.0
            maintence_value = 147.0
        elif lead.sheet_amount.value == '2 a 4 planilhas':
            implantation_value = 1500.0
            maintence_value = 297.0
        elif lead.sheet_amount.value == '5 ou mais planilhas':
            implantation_value = 3000.0
            maintence_value = 497.0

        offer = Offer(
            id=str(uuid.uuid4()),
            date=date.today(),
            expires_at=date.today().__add__(timedelta(days=7)),
            implantation_value=implantation_value,
            maintence_value=maintence_value,
            lead_id=lead.id
        )

        return self.repository.generate_offer(lead=lead, offer=offer)
