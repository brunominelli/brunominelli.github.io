from flask import Blueprint
from src.modules.site.presentation.controllers.site_controller import SiteController

class SiteRoutes:
    def __init__(self, controller:SiteController):
        self.controller = controller 
        self.blueprint = Blueprint("site", __name__)

        self.blueprint.add_url_rule("/", view_func=self.controller.landing_page, methods=["GET"])
        self.blueprint.add_url_rule("/auth", view_func=self.controller.auth_page, methods=["GET"])
        self.blueprint.add_url_rule("/success", view_func=self.controller.success_page, methods=["GET"])
        self.blueprint.add_url_rule("/dashboard", view_func=self.controller.dashboard_page, methods=["GET"])