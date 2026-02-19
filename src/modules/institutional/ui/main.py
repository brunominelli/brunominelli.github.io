import uuid
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.use_cases.create_use_case import CreateUseCase
from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.ui.controllers.lead_controller import LeadController

repository = JSONLeadRepository()
use_case = CreateUseCase(repository=repository)
create_controller = LeadController(use_case=use_case)

print('Create Lead')
lead = Lead()
lead.id = str(uuid.uuid4())
lead.lead = input('Lead: ')
lead.email = input('E-Mail: ')
lead.sheet_model = input('Sheet Model: ')
lead.sheet_amount = input('Sheet Amount: ')
lead.register_amount = int(input('Register Amount: '))
lead.register_type = input('Register Type: ')
lead.current_challenge = input('Current Challenge: ')

try:
    create_controller.create(lead=lead)
except Exception as error:
    raise error


