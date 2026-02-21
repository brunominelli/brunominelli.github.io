import os
import subprocess
import uuid
from src.modules.institutional.ui.di import build_institutional_containter
from src.modules.institutional.domain.entities.lead import Lead

def clear():
    subprocess.run('cls' if os.name == 'nt' else subprocess.run('clear'))

def pause():
    input('\nPress ENTER to continue...\n')

def safe_int_input(message:str, default:int | None = None) -> int:
    value = input(message)
    if not value and default is not None:
        return default
    return int(value)

def main():
    controllers = build_institutional_containter()

    while True:
        clear()

        print('\nCRUD Lead\n')

        print('1. Create Lead')
        print('2. Read All Leads')
        print('3. Read Lead By E-mail')
        print('4. Read Lead By ID')
        print('5. Update Lead')
        print('6. Delete Lead')
        print('0. Exit')

        option = input('Option: ')
        try: 
            if option == '1':
                clear()
                print('\nCreate Lead\n')

                lead = Lead(
                    id = str(uuid.uuid4()),
                    lead = input('Lead: '),
                    email = input('E-Mail: '),
                    sheet_model = input('Sheet Model: '),
                    sheet_amount = input('Sheet Amount: '),
                    register_amount = int(input('Register Amount: ')),
                    register_type = input('Register Type: '),
                    current_challenge = input('Current Challenge: '),
                )

                controllers['create'].create(lead=lead)

                print('Success: Lead created!')
                pause()
            
            elif option == '2':
                print('\nRead All\n')
                
                leads = controllers['read_all'].read_all()

                if not leads:
                    print('Leads not found.')
                else:
                    for lead in leads:
                        print(lead)

                pause()

            elif option == '3':
                print('\nRead By E-mail\n')

                email = input('E-mail: ')
                leads = controllers['read_by_email'].read_by_email(email=email)

                if not leads:
                    print('Leads not found.')
                    input('\nPress ENTER to continue')
                else:
                    for lead in leads:
                        print(lead)

                pause()

            elif option == '4':
                print('\nRead By ID\n')

                id = input('ID: ')
                lead = controllers['read_by_id'].read_by_id(id=id)

                if lead is None:
                    print('Lead not found')
                else:
                    print(lead)
                
                pause()

            elif option == '5':
                print('\nUpdate\n')

                id = input('ID: ')
                existing = controllers['read_by_id'].read_by_id(id=id)

                if existing is None:
                    print('Lead not found')
                    pause()
                    continue

                print('\n Leave blank to keep current value.\n')

                updated_lead = Lead(
                    id=existing.id,
                    lead=input(f'Lead ({existing.lead}): ') or existing.lead,
                    email=input(f'E-Mail ({existing.email}): ') or existing.email,
                    sheet_model=input(f'Sheet Model ({existing.sheet_model}): ') or existing.sheet_model,
                    sheet_amount=input(f'Sheet Amount ({existing.sheet_amount}): ') or existing.sheet_amount,
                    register_amount=safe_int_input(f'Register Amount ({existing.register_amount}): ', default=existing.register_amount),
                    register_type=input(f'Register Type ({existing.register_type}): ') or existing.register_type,
                    current_challenge=input(f'Current Challenge ({existing.current_challenge}): ') or existing.current_challenge,
                )

                controllers['update'].update(id=id, lead=updated_lead)

                print('\nSuccess: Lead updated!\n')
                pause()

            elif option == '6':
                print('\nDelete\n')

                id = input('ID: ')
                controllers['delete'].delete(id=id)

                print('Lead has been deleted')
                pause()

            elif option == '0':
                print('Bye!')
                break
            else:
                print('Invalid option!')
                pause()
        except Exception as error:
            print(f'\nError: {error}\n')
            pause()

if __name__ == '__main__':
    main()