from app import app
from flask import request
from flask_caching import Cache

from app.controllers import CommentController

# initialize cache
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app.app)


@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Comment Analyser</h1>" \
            "API available at <a href='/api/comments' target='_blank'>/api/comments</a><br />" \
            "Documentation available at <a href='/api/ui' target='_blank'>/api/ui</a><br />" \


# Connexion endpoints handled by Swagger


@app.route('/api/comments', methods=['POST'])
def create():
    """ create new comment """
    cc = CommentController()
    return cc.create(request=request)


@app.route('/api/comments', methods=['GET'])
@cache.cached(timeout=50)
def read():
    """ retrieves list of comments """

    cc = CommentController()
    return cc.read(request=request)


@app.route('/api/comments', methods=['PUT'])
def update():
    """ updates an existing comment """
    cc = CommentController()
    return cc.update(request=request)


@app.route('/api/comments', methods=['DELETE'])
def delete():
    """ deletes an existing comment """
    cc = CommentController()
    return cc.delete(request=request)
