from flask import Flask

from src.shared.injection.container import Container
from src.modules.lead.presentation.controllers.lead_controller import LeadController
from src.modules.site.presentation.controllers.site_controller import SiteController

from src.modules.lead.presentation.routes.lead_routes import LeadRoutes
from src.modules.site.presentation.routes.site_routes import SiteRoutes

class App:
    def create_app(self) -> Flask:
        app = Flask(
            __name__,
            template_folder="src/shared/templates",
            static_folder="src/shared/static"
        )

        app.secret_key = "1ec4b95660cbcfade4f4b75188b438e7a6b4934493a3aa6e35813b94fdcefbfb"

        # Injection
        container = Container()

        # Controllers
        site_controller = SiteController()
        lead_controller = LeadController(container=container)

        # Routs
        site_routes = SiteRoutes(controller=site_controller)
        lead_routes = LeadRoutes(controller=lead_controller)

        # Register blueprint
        app.register_blueprint(lead_routes.blueprint)
        app.register_blueprint(site_routes.blueprint)

        return app