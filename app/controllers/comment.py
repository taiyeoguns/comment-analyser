from datetime import datetime

from flask import jsonify

from app import db
from app.models import Comment
from app.services import ToneAnalyser


class CommentController:
    def __init__(self):
        self.ta = ToneAnalyser()

    def create(self, request):
        """ collects request parameters, gets tone from API
        and saves comment to database"""
        sku = request.form["sku"]
        text = request.form["text"]
        owner = request.form["owner"]
        timestamp = datetime.now()
        tone = self.ta.get_tone(text)

        comment = Comment(sku=sku, text=text, owner=owner, timestamp=timestamp, tone=tone)
        db.session.add(comment)
        db.session.commit()

        return jsonify({"id": str(comment.uuid), "timestamp": timestamp}), 201

    def read(self, request):
        """ gets lists of comments in database """
        comment_list = []

        comments = Comment.query.all()

        for comment in comments:
            comment_list.append(
                {
                    "id": comment.uuid,
                    "sku": comment.sku,
                    "text": comment.text,
                    "owner": comment.owner,
                    "tone": comment.tone,
                    "timestamp": comment.timestamp,
                }
            )

        return jsonify(comment_list), 200

    def update(self, request):
        pass

    def delete(self, request):
        pass
