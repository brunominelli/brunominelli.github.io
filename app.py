from dotenv import load_dotenv
from flask import Flask

from src.shared.injection.container import Container
from src.shared.auth.jwt_middleware import JwtMiddleware

# from src.modules.user.presentation.controllers.user_controller import UserController
# from src.modules.lead.presentation.controllers.lead_controller import LeadController
from src.modules.site.presentation.controllers.site_controller import SiteController

# from src.modules.user.presentation.routes.user_routes import UserRoutes
# from src.modules.lead.presentation.routes.lead_routes import LeadRoutes
from src.modules.site.presentation.routes.site_routes import SiteRoutes

class App:
    def create_app(self) -> Flask:
        load_dotenv()
        app = Flask(
            __name__,
            template_folder="src/shared/templates",
            static_folder="src/shared/static"
        )

        app.secret_key = "1ec4b95660cbcfade4f4b75188b438e7a6b4934493a3aa6e35813b94fdcefbfb"

        # Injection
        container = Container()

        # Middleware
        jwt_middleware = JwtMiddleware()
        jwt_middleware.init_app(app=app)

        # Controllers
        site_controller = SiteController(container=container)
        # user_controller = UserController(container=container)
        # lead_controller = LeadController(container=container)

        # Routs
        site_routes = SiteRoutes(controller=site_controller)
        # user_routes = UserRoutes(controller=user_controller)
        # lead_routes = LeadRoutes(controller=lead_controller)

        # Register blueprint
        # app.register_blueprint(user_routes.blueprint)
        # app.register_blueprint(lead_routes.blueprint)
        app.register_blueprint(site_routes.blueprint)

        return app