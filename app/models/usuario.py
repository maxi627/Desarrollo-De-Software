from dataclasses import dataclass
from typing import List
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User(db.Model):
    __tablename__ = 'users'  # Cambiado a 'users'

    id_user: int = db.Column('id', db.Integer, primary_key=True)
    nombre: str = db.Column('nombre', db.String(100), nullable=False)
    email: str = db.Column('email', db.String(120), unique=True, nullable=False)
    password: str = db.Column('password', db.String(100), nullable=False)
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
    
    # Encriptar password
    @property
    def password(self):
        raise AttributeError('password: campo de lectura no permitida')

    @password.setter
    def password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.__password, password)
