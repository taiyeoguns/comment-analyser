from flask import request
from . import routes
from app import cache
from app.controllers import CommentController


@routes.route("/", methods=["GET"])
def welcome():
    return (
        "<h1>Comment Analyser</h1>"
        "API available at <a href='/api/comments' target='_blank'>/api/comments</a><br />"
        "Documentation available at <a href='/api/ui' target='_blank'>/api/ui</a><br />"
    )


# Connexion endpoints handled by Swagger


@routes.route("/api/comments", methods=["POST"])
def create():
    """ create new comment """
    cc = CommentController()
    return cc.create(request=request)


@routes.route("/api/comments", methods=["GET"])
@cache.cached(timeout=50)
def read():
    """ retrieves list of comments """

    cc = CommentController()
    return cc.read(request=request)


@routes.route("/api/comments", methods=["PUT"])
def update():
    """ updates an existing comment """
    cc = CommentController()
    return cc.update(request=request)


@routes.route("/api/comments", methods=["DELETE"])
def delete():
    """ deletes an existing comment """
    cc = CommentController()
    return cc.delete(request=request)
