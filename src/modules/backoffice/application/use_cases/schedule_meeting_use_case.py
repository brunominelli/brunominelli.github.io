from datetime import datetime
from src.modules.backoffice.domain.entities.meeting import Meeting
from src.modules.backoffice.domain.repositories.i_meeting_repository import IMeetingRepository

class ScheduleMeetingUseCase:
    def __init__(self, repository:IMeetingRepository):
        self.respository = repository
    
    def execute(self, lead_id:str, date:datetime, notes:str) -> None:
        meeting = Meeting(lead_id=lead_id, date=date, notes=notes)
        self.respository.set_meeting(meeting=meeting)