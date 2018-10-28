import connexion

# add connexion
app = connexion.FlaskApp(__name__, specification_dir='../')
app.add_api('swagger.yml')

from app.routes import index
