import json

from src.modules.backoffice.domain.entities.meeting import Meeting
from src.modules.backoffice.domain.repositories.i_meeting_repository import IMeetingRepository

class JSONMeetingRepository(IMeetingRepository):
    def __init__(self):
        self.filepath = 'src/modules/backoffice/data/meeting.json'
    
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
    
    def _to_dict(self, meeting:Meeting) -> dict:
        return meeting._to_dict()
    
    def _to_entity(self, data:dict) -> Meeting:
        return Meeting(**data)
    
    def set_meeting(self, meeting:Meeting):
        data = self._load()
        data.append(self._to_dict(meeting=meeting))
        self._save(data=data)