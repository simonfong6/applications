from .companies import companies
from .data import data
from .users import users


def register_sub_site(app, prefix="/api"):
    app.register_blueprint(data, url_prefix=f'{prefix}/data')
    app.register_blueprint(users, url_prefix=f'{prefix}/users')
    app.register_blueprint(companies, url_prefix=f'{prefix}/companies')

