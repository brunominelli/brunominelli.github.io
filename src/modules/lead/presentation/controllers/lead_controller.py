import urllib.parse
from flask import request, jsonify, redirect, url_for
from src.shared.injection.container import Container
from src.modules.lead.application.dtos.lead_input_dto import LeadInputDTO
from src.modules.lead.application.dtos.lead_update_dto import LeadUpdateDTO
from src.modules.lead.application.dtos.lead_update_status_dto import LeadUpdateStatusDto

class LeadController:
    def __init__(self, container:Container):
        self.lead = container.lead
    
    def create(self):
        data = request.form

        if not data:
            raise Exception("JSON inválido")
        
        dto = LeadInputDTO(**data)
        self.lead.create.execute(dto=dto)

        return redirect(url_for("site.success_page"))
    
    def read_all(self):
        leads = self.lead.read_all.execute()
        return jsonify([lead.__dict__] for lead in leads), 200
    
    def read_by_id(self):
        data = request.json
        lead_id = data["lead_id"]

        lead = self.lead.read_by_id.execute(lead_id=lead_id)

        return jsonify(lead.__dict__), 200
    
    def read_kpis(self):
        kpis = self.lead.read_kpis.execute()
        return jsonify(kpis), 200

    def update(self):
        data = request.json
        dto = LeadUpdateDTO(**data)

        self.lead.update.execute(dto=dto)

        return jsonify({"message": "Lead atualizado com sucesso!"}), 200
    
    def update_status(self, lead_id:str):
        dto = LeadUpdateStatusDto(lead_id=lead_id, status="contacted")

        self.lead.update_status.execute(dto=dto)

        lead = self.lead.read_by_id.execute(lead_id=lead_id)
        
        message = f"""
            Olá {lead.name}!
            Recebi seu contato pelo site sobre a automação de {lead.subject}.
            Vamos conversar?"""

        encoded_message = urllib.parse.quote(message)
        clean_phone = "".join(filter(str.isdigit, lead.phone))

        if not clean_phone.startswith("55"):
            clean_phone = f"55{clean_phone}"

        whatsapp_url = f"https://wa.me/{clean_phone}?text={encoded_message}"

        return redirect(whatsapp_url)
    
    def delete(self):
        data = request.json
        lead_id = data["lead_id"]

        self.lead.delete.execute(lead_id=lead_id)
        return jsonify({"message": "Lead excluído com sucesso!"}), 204
