from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.value_objects.sheet_amount import SheetAmount

class ProposalService:
    def __init__(self, lead:Lead):
        self.lead = lead

    def generate_proposal(self) -> dict:
        problem = self.lead.current_problem or 'Processos manuais e falta de padronização'
        solution = {
            'Automação dos principais processos',
            'Organização da estrutura de dados e',
            'Redução de retrabalho operacional.'
        }

        estimated_price = self._set_estimated_price(lead=lead)

        return {
            'problema': problem,
            'solution': solution,
            'price': estimated_price,
            'deadline': '2 a 4 semanas'
        }
    
    def _set_estimated_price(self, lead:Lead) -> str:
        if lead.sheet_amount == SheetAmount.UP_TO_2:
            return ''
        elif lead.sheet_amount == SheetAmount.UP_TO_5:
            return ''
        elif lead.sheet_amount == SheetAmount.UP_TO_10:
            return ''
        elif lead.sheet_amount == SheetAmount.MORE_THAN_10:
            return ''
        else:
            raise ValueError('Erro na quantiadde de planilhas.')