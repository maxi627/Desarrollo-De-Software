from app.models import Usuario
from app import db

class UsuarioRepository:
    
    def __init__(self):
        self.__model = Usuario


    def get_all(self) -> list[Usuario]:
        return db.session.query(self.__model).all()

    
    def get_by_id(self, id) -> Usuario:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Usuario) -> Usuario:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Usuario) -> Usuario:
        entity = self.get_by_id(id)
        if entity:
            entity.password=t.password
            entity.email=t.email
            entity.nombre=t.nombre
            entity.id_pedido=t.id_pedido
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        usuario = self.get_by_id(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return Usuario
        return None
