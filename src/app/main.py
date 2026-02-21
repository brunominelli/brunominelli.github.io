from src.app.container import ApplicationContainer

container = ApplicationContainer()

create_lead = container.institutional.create_lead.execute()
