from app.models import Categorias
from app import db

class CategoriasRepository:
    def __init__(self):
        self.__model = Categorias

    def get_all(self) -> list[Categorias]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Categorias:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Categorias) -> Categorias:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Categorias) -> Categorias:
        entity = self.get_by_id(id)
        if entity:
            entity.id_categoria= t.id_categoria
            entity.nombre= t.nombre
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        categorias = self.get_by_id(id)
        if categorias:
            db.session.delete(categorias)
            db.session.commit()
            return categorias
        return None