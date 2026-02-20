import subprocess
import uuid
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.use_cases.create_use_case import CreateUseCase
from src.modules.institutional.domain.use_cases.read_all_use_case import ReadAllUseCase
from src.modules.institutional.data.repositories.json_lead_repository import JSONLeadRepository
from src.modules.institutional.ui.controllers.lead_controller import LeadController

repository = JSONLeadRepository()
create_use_case = CreateUseCase(repository=repository)
create_controller = LeadController(use_case=create_use_case)

read_all_use_case = ReadAllUseCase(repository=repository)
read_all_controller = LeadController(use_case=read_all_use_case)

while True:
    subprocess.run('clear')

    print('CRUD Lead')
    print('1. Create')
    print('2. Read All')
    print('3. Read By E-mail')
    print('4. Read By ID')
    print('5. Update')
    print('6. Delete')
    print('0. Exit')

    option = input('Option: ')

    if option == '1':
        subprocess.run('clear')

        print('Create Lead\n')
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
            print('Success: Lead has been created!')
            print('Press any button to continue')
            subprocess.run('clear')
        except Exception as error:
            print(f'Error> {error}')
    elif option == '2':
        print('Read All')
        try:
            leads = read_all_use_case.execute()
            if leads == []:
                print('There is no lead...')
                input('\nPress any key to continue')
            else:
                for lead in leads:
                    print(lead.__str__())
                input('\nPress any key to continue')
        except Exception as error:
            print(f'Error: {error}')
            input('\nPress any key to continue')
    elif option == '3':
        ...
    elif option == '4':
        ...
    elif option == '5':
        ...
    elif option == '6':
        ...
    elif option == '7':
        ...
    elif option == '0':
        print('Bye!')
        break
    else:
        print('Invalid option!')
        input('Press any button to continue')


