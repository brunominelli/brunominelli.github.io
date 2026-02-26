from enum import Enum

class SheetAmount(Enum):
    ONE_SHEET = '1 planilha'
    TWO_TO_FOUR_SHEETS = '2 a 4 planilhas'
    FIVE_PLUS_SHEETS = '5 ou mais planilhas'

    @classmethod
    def normalize(cls, value:str) -> 'SheetAmount':
        mapping = {
            '1': cls.ONE_SHEET,
            '2-4': cls.TWO_TO_FOUR_SHEETS,
            '5+': cls.FIVE_PLUS_SHEETS,
        }

        if value not in mapping:
            raise ValueError(f'Quantidade de planilhas inválida: {value}')
        return mapping[value]