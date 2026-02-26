from enum import Enum

class SheetTool(Enum):
    EXCEL = 'Excel'
    GOOGLE_SHEETS = 'Google Sheets'
    BOTH = 'Ambos'

    @classmethod
    def normalize(cls, value:str) -> 'SheetTool':
        mapping = {
            'excel': cls.EXCEL,
            'google_sheets': cls.GOOGLE_SHEETS,
            'both': cls.BOTH,
        }

        if value not in mapping:
            raise ValueError(f'Ferramenta inválida: {value}')
        return mapping[value]