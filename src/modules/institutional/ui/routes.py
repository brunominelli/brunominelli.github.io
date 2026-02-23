import uuid

from flask import Blueprint, render_template, request, redirect, url_for, flash

from src.app.container import ApplicationContainer
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.ui.forms import LeadForm

institutional = Blueprint(
    'institutional', 
    __name__, 
    template_folder='templates'
)

controller = ApplicationContainer().institutional

@institutional.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@institutional.route('/lead', methods=['POST'])
def create_lead():
    form = LeadForm(request.form)

    if not form.is_valid():
        for error in form.errors:
            flash(error)
        return redirect(url_for('institutional.index'))

    lead = Lead(**form.to_dict())
    controller.create_lead(lead=lead)

    return redirect(url_for('institutional.success'))

@institutional.route('/success')
def success():
    return render_template('success.html')
