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
        
        return render_template(
            "pages/dashboard/index.html", 
            leads=leads, 
            kpis=kpis
        )
