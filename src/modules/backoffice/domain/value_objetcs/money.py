class Money:
    def __init__(self, value:float):
        self.value = value
    
    def format(self) -> str:
        return f'R$ {self.value:,.2f}'.replace(',', '.')