from app import db
from dataclasses import dataclass, fields

@dataclass
class Orden(db.Model):
    __tablename__ = 'Detalle_Orden'

    id_detalle: int = db.Column('id_detalle', db.Integer, primary_key=True)
    id_pedido: int = db.Column('id_pedido', db.Integer, db.ForeignKey('Usuario.id_usuario'), nullable=False)  
    id_producto: int = db.Column('id_producto', db.Integer, db.ForeignKey('Producto.id_producto'), nullable=False)
    cantidad: int = db.Column('cantidad', db.Integer, nullable=False)
    precio: int = db.Column('precio', db.Integer, nullable=False)
    
    usuarios = db.relationship("Usuario", backref="usuario", lazy=True)