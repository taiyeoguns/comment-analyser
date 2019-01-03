import connexion
from os.path import abspath, dirname, join
from flask_sqlalchemy import SQLAlchemy

# add connexion
app = connexion.FlaskApp(__name__, specification_dir='../')

db_path = join(abspath(dirname(dirname(__file__))), 'database.db')
app.app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app.app)

# import models before create all
from app.models import Comment

db.create_all()

from app.routes import index

app.add_api('swagger.yml')
