from app import db
from dataclasses import dataclass

@dataclass
class Orden(db.Model):
    __tablename__ = 'Orden'

    id_detalle: int = db.Column('id_detalle',db.Integer, primary_key=True)
    id_pedido:  int = db.Column('id_pedido',db.Integer(100),db.ForeignKey(''), nullable=False)
    id_producto: int = db.Column('contenido',db.Integer,db.ForeignKey(''), nullable=False)
    cantidad: int = db.Column('cantidad',db.Integer, nullable=False)
    precio: int = db.Column('precio',db.Integer, nullable=False)
    
    
    
    # # Relación con el modelo Usuario
    # autor_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    # autor = db.relationship('Usuario', backref=db.backref('posts', lazy=True))
