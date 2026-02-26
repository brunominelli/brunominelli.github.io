from abc import ABC, abstractmethod

from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.entities.offer import Offer

class IOfferRepository(ABC):
    @abstractmethod
    def generate_offer(self, lead:Lead, offer:Offer) -> dict:
        ...