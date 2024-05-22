from dataclasses import dataclass
from app import db

@dataclass
class Producto(db.Model):
    __tablename__ = 'Producto'

    id_producto: int = db.Column('id_producto', db.Integer, primary_key=True)
    nombre: str = db.Column('nombre', db.Text, nullable=False)
    precio: int = db.Column('precio', db.Integer, nullable=False)
    stock: int = db.Column('stock', db.Integer, nullable=False)
    id_categoria: int = db.Column('id_categoria', db.Integer, db.ForeignKey('Categorias.id_categoria'), nullable=False) 
    
    # Relaciones
    ordenes = db.relationship('Orden', back_populates='producto', lazy=True)
    categoria = db.relationship('Categoria', back_populates='productos', lazy=True)
