from os.path import abspath, dirname, join
from app.services import ToneAnalyser, Database
from datetime import datetime
from flask import jsonify


class CommentController:
    def __init__(self):
        self.ta = ToneAnalyser()

        basedir = abspath(dirname(dirname(dirname(__file__))))
        self.db_location = join(basedir, 'database.db')

        with Database(self.db_location) as db:
            db.query(
                'create table if not exists comments (id INTEGER PRIMARY KEY AUTOINCREMENT, sku TEXT UNIQUE, text TEXT, owner TEXT, tone TEXT, timestamp DATETIME)'
            )

    def create(self, request):
        """ collects request parameters, gets tone from API and saves comment to database"""
        sku = request.form['sku']
        text = request.form['text']
        owner = request.form['owner']
        timestamp = datetime.now()
        tone = self.ta.get_tone(text)

        with Database(self.db_location) as db:
            db.query(
                'insert into comments (sku, text, owner, tone, timestamp) values (?, ?, ?, ?, ?)',
                params=(sku, text, owner, tone, timestamp))
            db.query('select last_insert_rowid() as rowid')
            data = db.fetchone()

        return jsonify({'id': str(data['rowid']), 'timestamp': timestamp}), 201

    def read(self, request):
        """ gets lists of comments in database """
        data = None
        data_list = []
        with Database(self.db_location) as db:
            db.query('select * from comments')
            data = db.fetchall()

        for dt in data:
            data_list.append({
                'id': dt['id'],
                'sku': dt['sku'],
                'text': dt['text'],
                'owner': dt['owner'],
                'tone': dt['tone'],
                'timestamp': dt['timestamp']
            })

        return jsonify(data_list), 200

    def update(self, request):
        pass

    def delete(self, request):
        pass
