from flask import Blueprint
from src.modules.lead.presentation.controllers.lead_controller import LeadController

class LeadRoutes:
    def __init__(self, controller:LeadController):
        self.controller = controller
        self.blueprint = Blueprint("lead", __name__, url_prefix="/leads")

        self.blueprint.add_url_rule("/create", view_func=self.controller.create, methods=["POST"])
        self.blueprint.add_url_rule("/read_all", view_func=self.controller.read_all, methods=["GET"])
        self.blueprint.add_url_rule("/read_by_id", view_func=self.controller.read_by_id, methods=["POST"])
        self.blueprint.add_url_rule("/read_kpis", view_func=self.controller.read_kpis, methods=["GET"])
        self.blueprint.add_url_rule("/update", view_func=self.controller.update, methods=["PUT"])
        self.blueprint.add_url_rule("/<string:lead_id>/update_status", view_func=self.controller.update_status, methods=["GET"])
        self.blueprint.add_url_rule("/delete", view_func=self.controller.delete, methods=["DELETE"])