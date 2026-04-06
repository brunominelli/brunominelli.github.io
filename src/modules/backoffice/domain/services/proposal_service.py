from src.modules.institutional.domain.entities.lead import Lead
from src.modules.backoffice.domain.services.pricing_policy import PricingPolicy
from src.modules.institutional.domain.value_objects.register_amount import RegisterAmount
from src.modules.institutional.domain.value_objects.register_type import RegisterType
from src.modules.institutional.domain.value_objects.sheet_amount import SheetAmount

class ProposalService:
    def __init__(self, lead:Lead, pricing_policy:PricingPolicy):
        self.lead = lead
        self.pricing_policy = pricing_policy
    
    def generate_proposal(self):
        score = self.pricing_policy.calculate_score(lead=self.lead)
        pricing = self.pricing_policy.calculate_pricing(score=score)
        problem = self._build_problem()

        types = [RegisterType.normalize(key=key) for key in self.lead.register_type]
        sheet_amount = SheetAmount.normalize(key=self.lead.sheet_amount)
        register_amount = RegisterAmount.normalize(key=self.lead.register_amount)
        
        context_parts = []
        context_parts.append(sheet_amount)
        context_parts.append(register_amount)
        context_parts.append(f'controles como {self._format_list(items=types)}')

        context = f'Atualmente sua operação envolve, {context_parts}.'

        solution = self._build_solution()

        return {
            'problem': problem,
            'context': context,
            'solution': solution,
            'complexity': pricing['complexity'],
            'price': pricing['price'],
            'deadline': pricing['deadline'],
        }
    
    def _build_problem(self):
        if self.lead.current_problem:
            return self.lead.current_problem

        return (
            "Dificuldade em manter a organização das informações, com presença de processos manuais "
            "e risco de inconsistência nos dados."
        )

    def _build_solution(self):
        return (
            "A proposta envolve a organização da estrutura de dados, padronização das planilhas "
            "e automação dos principais fluxos operacionais. O objetivo é reduzir retrabalho, "
            "minimizar erros e permitir que a operação cresça de forma mais previsível e controlada."
        )
    
    def _format_list(self, items):
        if not items:
            return ""

        if len(items) == 1:
            return items[0]

        return ", ".join(items[:-1]) + " e " + items[-1]