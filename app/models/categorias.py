from dataclasses import dataclass
from app import db

@dataclass
class Categoria(db.Model):
    __tablename__ = 'Categorias'

    id_categoria: int = db.Column('id_categoria', db.Integer, primary_key=True, autoincrement=True) 
    nombre: str = db.Column('nombre', db.Text, nullable=False)

    # Relaciones
    productos = db.relationship('Producto', back_populates='categoria', lazy=True)
