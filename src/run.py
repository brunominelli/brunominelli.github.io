# import subprocess
# from src.app.container import ApplicationContainer

# controller = ApplicationContainer()

# report_controller = controller.report
# personal_finance_controller = controller.personal_finance

# subprocess.run('clear')
# print('===== Cofre de Bolso =====')
# report = report_controller.generate_finance_report.execute(file_path='report.csv')
# personal_finance = personal_finance_controller.generate_personal_finance_report.execute(income=report.income)

# print(personal_finance)
# print(report)
from flask import Flask
from src.modules.institutional.ui.routes import institutional

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret'
    app.register_blueprint(institutional)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)