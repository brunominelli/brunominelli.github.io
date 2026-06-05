from flask import Blueprint
from src.modules.user.presentation.controllers.user_controller import UserController

class UserRoutes:
    def __init__(self, controller:UserController):
        self.controller = controller
        self.blueprint = Blueprint("user", __name__, url_prefix="/user")

        self.blueprint.add_url_rule("/login", view_func=self.controller.login, methods=["POST"])
        self.blueprint.add_url_rule("/logout", view_func=self.controller.logout, methods=["GET"])
        self.blueprint.add_url_rule("/create", view_func=self.controller.create, methods=["POST"])
        self.blueprint.add_url_rule("/read_all", view_func=self.controller.read_all, methods=["GET"])
        self.blueprint.add_url_rule("/read_by_id", view_func=self.controller.read_by_id, methods=["POST"])
        self.blueprint.add_url_rule("/read_by_email", view_func=self.controller.read_by_email, methods=["POST"])
        self.blueprint.add_url_rule("/update", view_func=self.controller.update, methods=["PUT"])
        self.blueprint.add_url_rule("/delete", view_func=self.controller.update, methods=["DELETE"])