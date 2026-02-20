import os
import json
from pathlib import Path
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.repositories.i_lead_repository import ILeadRepository

class JSONLeadRepository(ILeadRepository):
    def __init__(self, file_path:str = None):
        if file_path is None:
            self.file_path = Path('src/modules/institutional/data/leads.json')
        else:
            self.file_path = Path(file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file, indent=4)
        else:
            try:
                with open(self.file_path, 'r', encoding='utf-8') as file:
                    json.load(file)
            except json.JSONDecodeError:
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    json.dump([], file, indent=4)

    def create(self, lead:Lead) -> None:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            leads:list = json.load(file)
        
        leads.append(lead.__dict__)

        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(leads, file, indent=4)
    
    def read_all(self) -> list[Lead]:
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data:list = json.load(file)
            leads:list[Lead] = []
        for item in data:
            leads.append(
                Lead(
                    id=item['id'],
                    lead=item['lead'],
                    email=item['email'],
                    sheet_model=item['sheet_model'],
                    sheet_amount=item['sheet_amount'],
                    register_amount=item['register_amount'],
                    register_type=item['register_type'],
                    current_challenge=item['current_challenge']
                )
            )
        return leads
    
    def read_by_email(self, email) -> list[Lead]:
        return super().read_by_email(email)
    
    def read_by_id(self, id) -> Lead:
        return super().read_by_id(id)
    
    def update(self, id, lead) -> None:
        return super().update(id, lead)
    
    def delete(self, id, lead) -> None:
        return super().delete(id, lead)