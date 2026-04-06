from abc import ABC, abstractmethod
from src.modules.backoffice.domain.entities.meeting import Meeting

class IMeetingRepository(ABC):
    @abstractmethod
    def set_meeting(self, meeting:Meeting) -> None: ...