from enum import Enum

class RegisterAmount(Enum):
    UP_TO_300 = 'Até 300 registros'
    BETWEEN_300_AND_1000 = 'Entre 300 e 1000 registros'
    MORE_THAN_1000 = 'Mais de 1000 registros'

    @classmethod
    def normalize(cls, value:str) -> 'RegisterAmount':
        mapping = {
            'ate_300': cls.UP_TO_300,
            '300_1000': cls.BETWEEN_300_AND_1000,
            '1000+': cls.MORE_THAN_1000,
        }

        if value not in mapping:
            raise ValueError(f'Valor médio de registros inválido: {value}')
        return mapping[value]