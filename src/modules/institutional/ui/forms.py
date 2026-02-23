import re

class LeadForm:
    def __init__(self, form_data: dict):
        self.errors = []

        self.lead = form_data.get('lead_name', '')
        self.email = form_data.get('lead_email', '')
        self.sheet_model = form_data.get('leed_sheet_model', '')
        self.sheet_amount = form_data.get('leed_sheet_amount', '')
        self.register_amount = form_data.get('leed_register_amount', '')
        self.register_type = form_data.get('lead_register_type', '')
        self.current_challenge = form_data.get('lead_current_challenge')

        self._validate()

    def _validate(self):
        if not self.lead:
            self.errors.append('Nome/Empresa é obrigatório.')
        
        if not self.email:
            self.errors.append('E-mail é obrigatório.')
        else:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern=pattern, string=self.email):
                self.errors.append('E-mail inválido')
        
        if not self.sheet_model:
            self.errors.append('Selecione o modelo de planilha.')
        
        if not self.sheet_amount:
            self.errors.append('Informe a quantidade média de planilhas.')
        
        if not self.register_amount:
            self.errors.append('Informe a quantidade de planilhas.')
        
        if not self.register_type:
            self.errors.append('Informe o(s) tipo(s) de registro(s).')
        
        if not self.current_challenge:
            self.errors.append('Descreva seu desafio atual.')
    
    def is_valid(self):
        return len(self.errors) == 0
    
    def to_dict(self):
        return {
            'lead': self.lead,
            'email': self.email,
            'sheet_model': self.sheet_model,
            'sheet_amount': self.sheet_amount,
            'register_amount': self.register_amount,
            'register_type': self.register_type,
            'current_challenge': self.current_challenge,
        }