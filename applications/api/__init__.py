from .companies import companies
from .data import data
from .jobs import jobs
from .users import users


def register_sub_site(app, prefix="/api"):
    app.register_blueprint(companies, url_prefix=f'{prefix}/companies')
    app.register_blueprint(data, url_prefix=f'{prefix}/data')
    app.register_blueprint(jobs, url_prefix=f'{prefix}/jobs')
    app.register_blueprint(users, url_prefix=f'{prefix}/users')
