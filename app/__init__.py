import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config import Config


db = SQLAlchemy()
cache = Cache(config={"CACHE_TYPE": "simple"})


def create_app(cfg=Config):
    # add connexion
    app = connexion.FlaskApp(__name__, specification_dir="../")
    flaskapp = app.app  # get flask app object

    # configure database
    flaskapp.config.from_object(cfg)

    # initialize database
    db.init_app(flaskapp)

    # initialize cache
    cache.init_app(flaskapp)

    from app.routes import routes as routes_bp  # noqa

    flaskapp.register_blueprint(routes_bp)

    # import models before create all
    from app.models import Comment  # noqa

    with flaskapp.app_context():
        db.create_all()

    app.add_api("swagger.yml")

    return app


flaskapp = create_app().app  # for flask run
