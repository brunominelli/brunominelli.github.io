from enum import Enum

class RegisterAmount(Enum):
    UP_TO_500 = 'até 500 registros'
    UP_TO_2000 = 'entre 500 e 2000 registros'
    UP_TO_5000 = 'entre 2000 e 5000 registros'
    MORE_THAN_5000 = 'mais de 5000 registros'

    @classmethod
    def normalize(cls, key:str) -> str:
        mapping = {
            'up_to_500': cls.UP_TO_500,
            'up_to_2000': cls.UP_TO_2000,
            'up_to_5000': cls.UP_TO_5000,
            'more_than_5000': cls.MORE_THAN_5000,
        }

        if key not in mapping:
            raise ValueError(f'Invalid data: {key}')
        return str(mapping[key].value)
