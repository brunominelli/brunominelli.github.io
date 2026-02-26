from enum import Enum

class RegisterType(Enum):
    FINANCE = 'Financeiro'
    CLIENTS = 'Clientes'
    PROJECTS = 'Projetos'
    STORAGE = 'Estoque'
    FINANCE_CLIENTS = 'Financeiro + Clientes'
    FINANCE_PROJECTS = 'Financeiro + Projetos'
    OHTERS = 'Outros'

    @classmethod
    def normalize(cls, value:str) -> 'RegisterType':
        mapping = {
            'financeiro': cls.FINANCE,
            'clientes': cls.CLIENTS,
            'projetos': cls.PROJECTS,
            'estoque': cls.STORAGE,
            'financeiro_clientes': cls.FINANCE_CLIENTS,
            'financeiro_projetos': cls.FINANCE_PROJECTS,
            'outros': cls.OHTERS
        }

        if value not in mapping:
            raise ValueError(f'Tipo de registro inválido: {value}')
        return mapping[value]