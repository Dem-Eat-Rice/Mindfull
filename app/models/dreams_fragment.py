from .db import db


class Dreams_Fragment(db.Model):
    __tablename__ = 'dreams_fragments'

    id = db.Column(db.Integer, primary_key=True)
    dream_id = db.Column(db.Integer, db.ForeignKey(
        'dreams.id'), nullable=False)
    fragment_id = db.Column(
        db.Integer, db.ForeignKey('fragments.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'dream_id': self.dream_id,
            'fragment_id': self.fragment_id
        }
