from flask import Blueprint, render_template
from src.app.container import ApplicationContainer

backoffice = Blueprint('backoffice', __name__, template_folder='templates')
container = ApplicationContainer()