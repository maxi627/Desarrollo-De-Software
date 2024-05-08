from app import db
from dataclasses import dataclass

@dataclass
class Like(db.Model):
    __tablename__ = 'likes'

    id: int = db.Column("id",db.Integer, primary_key=True, autoincrement=True)
    post_id: int = db.Column('post_id',db.Integer, db.ForeignKey('posts.id'), nullable=False)
    usuario_id: int = db.Column('usuario_id',db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
