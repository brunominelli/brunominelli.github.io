import urllib.parse
from flask import render_template
from src.shared.injection.container import Container

class SiteController:
    def __init__(self, container:Container):
        self.lead = container.lead
    
    def landing_page(self):
        return render_template("pages/landing/index.html")
    
    def success_page(self):
        return render_template("pages/landing/success.html")
    
    def dashboard_page(self):
        leads = self.lead.read_all.execute()
        kpis = self.lead.read_kpis.execute()

        for lead in leads:
            message = f"""
            Olá {lead.name}!
            Recebi seu contato pelo site sobre a automação de {lead.subject}.
            Vamos conversar?"""

            encoded_message = urllib.parse.quote(message)
            clean_phone = "".join(filter(str.isdigit, lead.phone))

            if not clean_phone.startswith("55"):
                clean_phone = f"55{clean_phone}"
                
            lead.whatsapp_url = f"https://wa.me/{clean_phone}?text={encoded_message}"
        
        return render_template(
            "pages/dashboard/index.html", 
            leads=leads, 
            kpis=kpis
        )
