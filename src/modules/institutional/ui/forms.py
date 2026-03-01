import re

from src.modules.institutional.domain.dtos.create_lead_dto import CreateLeadDTO

class LeadForm:
    def __init__(self, lead_dto: CreateLeadDTO):
        self.errors = []
        self.lead_dto = lead_dto

        self._validate()

    def _validate(self):
        if not self.lead_dto.lead:
            self.errors.append('Nome/Empresa é obrigatório.')
        
        if not self.lead_dto.email:
            self.errors.append('E-mail é obrigatório.')
        else:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern=pattern, string=self.lead_dto.email):
                self.errors.append('E-mail inválido')
        
        if not self.lead_dto.sheet_tool:
            self.errors.append('Selecione o modelo de planilha.')
        
        if not self.lead_dto.sheet_amount:
            self.errors.append('Informe a quantidade média de planilhas.')
        
        if not self.lead_dto.register_amount:
            self.errors.append('Informe a quantidade de planilhas.')
        
        if not self.lead_dto.register_type:
            self.errors.append('Informe o(s) tipo(s) de registro(s).')
        
        if not self.lead_dto.current_challenge:
            self.errors.append('Descreva seu desafio atual.')
    
    def is_valid(self):
        return len(self.errors) == 0
    
    def to_dict(self):
        return {
            'id': self.lead_dto.id,
            'lead': self.lead_dto.lead,
            'email': self.lead_dto.email,
            'sheet_tool': self.lead_dto.sheet_tool,
            'sheet_amount': self.lead_dto.sheet_amount,
            'register_amount': self.lead_dto.register_amount,
            'register_type': self.lead_dto.register_type,
            'current_challenge': self.lead_dto.current_challenge,
        }