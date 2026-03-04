from enum import Enum

class RegisterType(Enum):
    FINANCE = 'Finanças'
    PROJECTS = 'Projetos'
    CLIENTS = 'Clientes'
    STORAGE = 'Estoque'
    SALES = 'Vendas'
    OTHERS = 'Outros'

    def normalize(self, key:str) -> str:
        mapping = {
            'finance': self.FINANCE,
            'projects': self.PROJECTS,
            'clients': self.CLIENTS,
            'storage': self.STORAGE,
            'sales': self.SALES,
            'others': self.OTHERS,
        }

        if key not in mapping[key]:
            raise ValueError(f'Invalid data: {key}')
        return str(mapping[key].value)