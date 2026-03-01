import uuid

from flask import Blueprint, render_template, request, redirect, url_for, flash

from src.app.container import ApplicationContainer
from src.modules.institutional.domain.dtos.create_lead_dto import CreateLeadDTO
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

    input_dto = CreateLeadDTO(
        id = str(uuid.uuid4()),
        lead = request.form.get('lead_name', ''),
        email = request.form.get('lead_email', ''),
        sheet_tool = request.form.get('leed_sheet_tool', ''),
        sheet_amount = request.form.get('leed_sheet_amount', ''),
        register_amount = request.form.get('leed_register_amount', ''),
        register_type = request.form.get('lead_register_type', ''),
        current_challenge = request.form.get('lead_current_challenge'),
    )

    form = LeadForm(lead_dto=input_dto)

    if not form.is_valid():
        for error in form.errors:
            flash(error)
        return redirect(url_for('institutional.index'))

    lead = controller.create_lead.execute(input_dto=input_dto)
    controller.generate_offer.execute(lead=lead)

    return redirect(url_for('institutional.success'))

@institutional.route('/success')
def success():
    return render_template('success.html')
