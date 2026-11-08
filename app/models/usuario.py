from dataclasses import dataclass
from typing import List
from app import db

@dataclass
class User(db.Model):
    __tablename__ = 'users'  # Cambiado a 'users'

    id_user: int = db.Column('id', db.Integer, primary_key=True)
    nombre: str = db.Column('nombre', db.String(100), nullable=False)
    email: str = db.Column('email', db.String(120), unique=True, nullable=False)
    # Guarda el hash de la contraseña. El hash lo genera UserService con SecurityManager
    # (los hashes de werkzeug/passlib superan los 100 caracteres, por eso 255).
    password: str = db.Column('password', db.String(255), nullable=False)
    id_detalle: int = db.Column('id_detalle', db.Integer, db.ForeignKey('Detalle_Orden.id_detalle'), nullable=True)

    # Relaciones
    ordenes = db.relationship('Orden', back_populates='user', lazy=True)

    def save(self) -> 'User':
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def all(cls) -> List['User']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'User':
        return db.session.get(cls, id)
    
    @classmethod
    def find_by(cls, **kwargs) -> List['User']:
        return cls.query.filter_by(**kwargs).all()

    # El hash y la verificación de la contraseña están en app/services/security.py
    # (SecurityManager). Antes había acá una @property "password" que pisaba la
    # columna, y la contraseña nunca se guardaba en la base.
