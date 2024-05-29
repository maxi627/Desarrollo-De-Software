from app.models import Categoria
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete


class CategoriaRepository(Repository_create,Repository_delete,Repository_update,Repository_get):
    def __init__(self):
        self.__model = Categoria

    def get_all(self) -> list[Categoria]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Categoria:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Categoria) -> Categoria:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Categoria) -> Categoria:
        entity = self.get_by_id(id)
        if entity:
            entity.id_categoria= t.id_categoria
            entity.nombre= t.nombre
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        Categoria = self.get_by_id(id)
        if Categoria:
            db.session.delete(Categoria)
            db.session.commit()
            return Categoria
        return None