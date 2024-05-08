from app import db
from dataclasses import dataclass

@dataclass
class Categoria(db.Model):
    __tablename__ = 'Categorias'

    id_categoria: int = db.Column("id_categoria", db.Integer, primary_key=True, autoincrement=True) 
    nombre: str = db.Column('nombre',db.Text, db.ForeignKey(''), nullable=False)


