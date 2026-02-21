from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.domain.use_cases.create_use_case import CreateUseCase
from src.modules.institutional.domain.use_cases.read_all_use_case import ReadAllUseCase
from src.modules.institutional.domain.use_cases.read_by_id_use_case import ReadByIdUseCase
from src.modules.institutional.domain.use_cases.read_by_email_use_case import ReadByEmailUseCase
from src.modules.institutional.domain.use_cases.update_use_case import UpdateUseCase
from src.modules.institutional.domain.use_cases.delete_use_case import DeleteUseCase
from src.modules.institutional.ui.controllers.lead_controller import LeadController

def build_institutional_containter():
    repository = JSONLeadRepository()
    return {
        'create': LeadController(use_case=CreateUseCase(repository=repository)),
        'read_all': LeadController(use_case=ReadAllUseCase(repository=repository)),
        'read_by_id': LeadController(use_case=ReadByIdUseCase(repository=repository)),
        'read_by_email': LeadController(use_case=ReadByEmailUseCase(repository=repository)),
        'update': LeadController(use_case=UpdateUseCase(repository=repository)),
        'delete': LeadController(use_case=DeleteUseCase(repository=repository))
    }