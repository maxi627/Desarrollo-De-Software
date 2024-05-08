
from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass
class Comentario(db.Model):
    __tablename__ = 'comentarios'

    id: int = db.Column('id',db.Integer, primary_key=True)
    contenido: str = db.Column('contenido',db.Text, nullable=False)
    fecha_creacion: datetime = db.Column('fecha_creacion',db.DateTime, nullable=False, default=datetime.utcnow)

    autor_id: int = db.Column('autor_id',db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    autor = db.relationship('Usuario', backref=db.backref('comentarios', lazy=True))

    post_id: int = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('comentarios', lazy=True))
