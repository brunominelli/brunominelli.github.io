from flask import render_template

class SiteController:
    def landing_page(self):
        return render_template("pages/landing/index.html")
    
    def success_page(self):
        return render_template("pages/landing/success.html")
