import json

from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class JSONLeadRepository(ILeadRepository):
    def __init__(self):
        self.filepath = 'src/modules/institutional/data/leads.json'

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
    
    def _to_dict(self, lead:Lead) -> dict:
        return lead._to_dict()
    
    def _to_entity(self, data:dict) -> Lead:
        return Lead(**data)
    
    def create(self, lead:Lead) -> Lead:
        data = self._load()
        data.append(self._to_dict(lead=lead))
        self._save(data=data)
        return lead
    
    def read(self) -> list[Lead]:
        data = self._load()
        leads = [self._to_entity(data=item) for item in data]
        return leads
    
    def read_by_id(self, id:str) -> Lead:
        data = self._load()
        lead = next((self._to_entity(data=item) for item in data if item['id'] == id), None)
        return lead
    
    def update(self, id:str, lead:Lead) -> None:
        data = self._load()
        updated = False

        for index, item in enumerate(data):
            if item['id'] == id:
                data[index] = self._to_dict(lead=lead)
                updated = True
                break
        if not updated:
            raise ValueError('Lead not found')
        
        self._save(data=data)

    def delete(self, id:str) -> None:
        data = self._load()
        new_data = [item for item in data if item['id'] != id]

        if len(new_data) == data:
            raise ValueError('Lead not found')
        
        self._save(data=data)
