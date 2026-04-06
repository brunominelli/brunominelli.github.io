from src.modules.institutional.domain.entities.lead import Lead

class PricingPolicy:
    SHEET_SCORE = {
        'up_to_2': 1,
        'up_to_5': 2,
        'up_to_10': 3,
        'more_than_10': 4,
    }

    REGISTER_SCORE = {
        'up_to_500': 1,
        'up_to_2000': 2,
        'up_to_5000': 3,
        'more_than_5000': 4,
    }

    COMPLEXITY_SCORE = {
        'finance': 2,
        'sales': 2,
        'storage': 2,
        'projects': 3,
        'clients': 1,
        'others': 1,
    }

    def calculate_score(self, lead:Lead) -> dict:
        score = 0
        score += self.SHEET_SCORE.get(lead.sheet_amount, 0)
        score += self.REGISTER_SCORE.get(lead.register_amount, 0)
        
        for type in lead.register_type:
            score += self.COMPLEXITY_SCORE.get(type, 0)

        return score

    def calculate_pricing(self, score: int):
        if score <= 4:
            return {"price": "R$ 1.500", "deadline": "1 a 2 semanas", "complexity": "Baixa"}

        if score <= 8:
            return {"price": "R$ 3.000", "deadline": "2 a 3 semanas", "complexity": "Média"}

        if score <= 12:
            return {"price": "R$ 5.000", "deadline": "3 a 5 semanas", "complexity": "Alta"}

        return {"price": "R$ 8.000", "deadline": "5 semanas", "complexity": "Muito Alta"}