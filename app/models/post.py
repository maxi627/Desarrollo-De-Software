from app import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Post(db.Model):
    __tablename__ = 'posts'

    id: int = db.Column('id',db.Integer, primary_key=True)
    titulo: str = db.Column('titulo',db.String(100), nullable=False)
    contenido: str = db.Column('contenido',db.Text, nullable=False)
    fecha_creacion: datetime = db.Column('fecha_creacion',db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relación con el modelo Usuario
    autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    autor = db.relationship('Usuario', backref=db.backref('posts', lazy=True))
