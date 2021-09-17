from app import db


class Post(db.Model):
    webhook_id = db.Column(db.String(50), primary_key=True)
    ip_address = db.Column(db.String(50))
    apikey = db.Column(db.String(50))
    status = db.Column(db.String(50))

    def __repr__(self):
        return '<Post {}>'.format(self.webhook_id)
