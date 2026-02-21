import os
import json
from pathlib import Path
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class JSONLeadRepository(ILeadRepository):
    def __init__(self, file_path:str | None = None):
        self.file_path = Path(file_path or Path('src/modules/institutional/data/leads.json'))
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.file_path.exists():
            self._save([])
    
    def _save(self, data:list[dict]) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
    
    def _load(self) -> list[dict]:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def _to_entity(self, item:dict) -> Lead:
        return Lead(**item)

    def _to_dict(self, lead:Lead) -> dict:
        return lead.__dict__

    def create(self, lead:Lead) -> None:
        data = self._load()
        data.append(self._to_dict(lead=lead))
        self._save(data=data)
    
    def read_all(self) -> list[Lead]:
        return [self._to_entity(item=item) for item in self._load()]
    
    def read_by_email(self, email:str) -> list[Lead]:
        return [self._to_entity(item=item) for item in self._load()]
    
    def read_by_id(self, id:str) -> Lead:
        for item in self._load():
            if item['id'] == id:
                return self._to_entity(item=item)
        return None
    
    def update(self, id:str, lead:Lead) -> None:
        data = self._load()
        for index, item in enumerate(data):
            if item['id'] == id:
                data[index] = self._to_dict(lead=lead)
                self._save(data=data)
                return
        raise Exception('Lead not found')
    
    def delete(self, id:str) -> None:
        data = self._load()
        new_data = [item for item in data if item['id'] != id]
        self._save(data=new_data)
