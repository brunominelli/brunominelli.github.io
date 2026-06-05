from src.shared.injection.lead_container import LeadContainer
from src.shared.injection.user_container import UserContainer

class Container:
    def __init__(self):
        self.lead = LeadContainer()
        self.user = UserContainer()