from app import db
from dataclasses import dataclass

@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id: int = db.Column('id',db.Integer, primary_key=True)
    nombre: str = db.Column('nombre',db.String(100), nullable=False)
    email: str = db.Column('email',db.String(120), unique=True, nullable=False)
    contrasena: str= db.Column('contrasena',db.String(100), nullable=False)
    id_pedido: int= db.colummn('id_pedido',db.integer,db.ForeignKey(''),unique=True,nullable=False)
