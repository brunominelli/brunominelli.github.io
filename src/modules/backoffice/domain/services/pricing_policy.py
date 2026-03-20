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
        'projects': 1,
        'clients': 1,
        'others': 1,
    }

    def calculate_score(self, lead:Lead) -> dict:
        sheet_score = self.SHEET_SCORE.get(lead.sheet_amount, 1)
        register_score = self.REGISTER_SCORE.get(lead.register_amount, 1)
        
    def calculate_pricing(self, score:int) -> dict:...