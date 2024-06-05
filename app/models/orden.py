from app import db
from dataclasses import dataclass

@dataclass
class Orden(db.Model):
    __tablename__ = 'Detalle_Orden'

    id_detalle = db.Column('id_detalle',db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, db.ForeignKey('Producto.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Integer, nullable=False)
    
    # Relaciones
    usuario = db.relationship('Usuario', back_populates='ordenes', lazy=True )
    producto = db.relationship('Producto', back_populates='ordenes',lazy=True)
