import json
from src.modules.backoffice.domain.entities.proposal import Proposal
from src.modules.backoffice.domain.repositories.i_proposal_repository import IProposalRepository

class JSONProposalRepository(IProposalRepository):
    def __init__(self):
        self.filepath = 'src/modules/backoffice/data/proposal.json'
    
    def _load(self) -> list:
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except (FileExistsError, json.JSONDecodeError):
            return []
    
    def _save(self, data:list) -> None:
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def _to_dict(self, proposal:Proposal) -> dict:
        return proposal._to_dict()
    
    def _to_entity(self, data:dict) -> Proposal:
        return Proposal(**data)
    
    def create(self, proposal:Proposal) -> Proposal:
        data = self._load()
        data.append(self._to_dict(proposal=proposal))
        self._save(data=data)
        return proposal

    def get_by_lead_id(self, lead_id:str):
        data = self._load()
        for item in data:
            if item['lead_id'] == lead_id:
                return self._to_entity(item)
        return None