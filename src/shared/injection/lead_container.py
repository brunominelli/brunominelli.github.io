from src.modules.lead.infrastructure.repositories.user_sqlite_repository import UserSQLiteRepository
from src.modules.lead.application.use_cases.create_lead_use_case import CreateLeadUseCase
from src.modules.lead.application.use_cases.read_all_lead_use_case import ReadAllLeadUseCase
from src.modules.lead.application.use_cases.read_lead_by_id_use_case import ReadLeadByIdUseCase
from src.modules.lead.application.use_cases.read_kpis_use_case import ReadKpisUseCase
from src.modules.lead.application.use_cases.update_use_case import UpdateLeadUseCase
from src.modules.lead.application.use_cases.delete_lead_use_case import DeleteLeadUseCase

class LeadContainer:
    def __init__(self):
        self.repository = UserSQLiteRepository()

        self.create = CreateLeadUseCase(repository=self.repository)
        self.read_all = ReadAllLeadUseCase(repository=self.repository)
        self.read_by_id = ReadLeadByIdUseCase(repository=self.repository)
        self.read_kpis = ReadKpisUseCase(repository=self.repository)
        self.update = UpdateLeadUseCase(repository=self.repository)
        self.delete = DeleteLeadUseCase(repository=self.repository)