from flask import Flask

from src.shared.injection.container import Container
from src.modules.lead.presentation.controllers.lead_controller import LeadController
from src.modules.lead.presentation.routes.lead_routes import LeadRoutes

class App:
    def create_app(self) -> Flask:
        app = Flask(
            __name__,
            template_folder="src/shared/templates",
            static_folder="src/shared/static"
        )

        # Injection
        container = Container()

        # Controllers
        lead_controller = LeadController(container=container)

        # Routs
        lead_routes = LeadRoutes(controller=lead_controller)

        # Register blueprint
        app.register_blueprint(lead_routes.blueprint)

        return app