class Deadline:
    def __init__(self, weeks:int):
        self.weeks = weeks
    
    def format(self) -> str:
        if self.weeks == 1:
            return '1 semana'
        return f'{self.weeks} a {self.weeks + 1} semanas'