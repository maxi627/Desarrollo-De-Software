from dataclasses import dataclass, field
from typing import List
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class Usuario(db.Model):
    __tablename__ = 'Usuario'

    id: int = db.Column('id',db.Integer, primary_key=True)
    nombre: str = db.Column('nombre',db.String(100), nullable=False)
    email: str = db.Column('email',db.String(120), unique=True, nullable=False)
    password: str= db.Column('password',db.String(100), nullable=False)
    id_pedido: int= db.Column('id_pedido',db.Integer,db.ForeignKey('Detalle_Orden.id_pedido'),unique=True,nullable=False)



    def save(self) -> 'Usuario':
        db.session.add(self)
        db.session.commit()
        return self
    
    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def all(cls) -> List['Usuario']:
        return cls.query.all()

    @classmethod
    def find(cls, id: int) -> 'Usuario':
        return db.session.get(cls, id)
    
    @classmethod
    def find_by(cls, **kwargs) -> List['Usuario']:
        return cls.query.filter_by(**kwargs).all()
    
    """
    Encriptar password para cumplir con la tarea de seguridad #16
    """
    #TODO: Refactorizar el código para que sea más legible y mantenible utilizando los principios SOLID.
    @property
    def password(self):
        raise AttributeError('password: campo de lectura no permitida')

    @password.setter
    def password(self, password):
        self.__password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.__password, password)


