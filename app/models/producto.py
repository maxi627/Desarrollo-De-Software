
from dataclasses import dataclass

from app import db

@dataclass
class Producto(db.Model):
    __tablename__ = 'Producto'

    id_producto: int = db.Column('id_producto',db.Integer, primary_key=True)
    nombre: str = db.Column('nombre',db.Text, nullable=False)
    precio: int = db.Column('precio',db.integer, nullable=False)
    stock: int= db.column('stock',db.integer,nullable=False)
    id_categoria: int = db.Column('id_categoria',db.Integer, db.ForeignKey(''), nullable=False)
    
    # autor = db.relationship('Usuario', backref=db.backref('comentarios', lazy=True))

    # post_id: int = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    # post = db.relationship('Post', backref=db.backref('comentarios', lazy=True))
