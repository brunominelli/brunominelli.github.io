import uuid
from flask import Blueprint, request, redirect, render_template, flash, url_for
from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.dtos.input_lead_dto import InputLeadDTO
from src.app.container import ApplicationContainer

container = ApplicationContainer()

institutional = Blueprint(
    'institutional',
    __name__,
    template_folder='templates'
)

@institutional.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@institutional.route('/success', methods=['GET'])
def success():
    return render_template('success.html')

@institutional.route('/lead', methods=['POST'])
def create_lead():
    dto = InputLeadDTO(
        lead=request.form.get('lead_name', ''),
        email=request.form.get('lead_email', ''),
        sheet_amount=request.form.get('lead_sheet_amount', ''),
        register_amount=request.form.get('lead_register_amount', ''),
        register_type=request.form.getlist('lead_register_type'),
        current_problem=request.form.get('lead_current_problem', ''),
    )

    container.institutional.create_lead.execute(dto=dto)
    return redirect(url_for('institutional.success'))
