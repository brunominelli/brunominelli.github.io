from enum import Enum

class RegisterType(Enum):
    FINANCE = 'Finanças'
    PROJECTS = 'Projetos'
    CLIENTS = 'Clientes'
    STORAGE = 'Estoque'
    SALES = 'Vendas'
    OTHERS = 'Outros'

    @classmethod
    def normalize(cls, key:str) -> str:
        mapping = {
            'finance': cls.FINANCE,
            'projects': cls.PROJECTS,
            'clients': cls.CLIENTS,
            'storage': cls.STORAGE,
            'sales': cls.SALES,
            'others': cls.OTHERS,
        }

        if key not in mapping:
            raise ValueError(f'Invalid data: {key}')
        return str(mapping[key].value)