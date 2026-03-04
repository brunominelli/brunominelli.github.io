from enum import Enum

class SheetAmount(Enum):
    UP_TO_2 = '1 a 2 planilhas'
    UP_TO_5 = '3 a 5 planilhas'
    UP_TO_10 = '6 a 10 planilhas'
    MORE_THEN_10 = 'mais de 10 planilhas'

    def normalize(self, key:str) -> str:
        mapping = {
            'up_to_2': self.UP_TO_2,
            'up_to_5': self.UP_TO_5,
            'up_to_10': self.UP_TO_10,
            'more_then_10': self.MORE_THEN_10,
        }

        if key not in mapping[key]:
            raise ValueError(f'Invalid data: {key}')
        
        return str(mapping[key].value)