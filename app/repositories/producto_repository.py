
from app.models import Producto
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class ProductoRepository(Repository_create,Repository_delete,Repository_update,Repository_get,Repository_save):
    def __init__(self):
        self.__model = Producto 
        
    def get_all(self) -> list[Producto]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Producto:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Producto) -> Producto:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Producto) -> Producto:
        entity = self.get_by_id(id) 
        if entity: 
            entity.id_producto=t.id_producto
            entity.nombre=t.nombre
            entity.precio=t.precio
            entity.stock=t.stock
            entity.id_categoria=t.id_categoria
            
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        producto = self.get_by_id(id) 
        if producto: 
            db.session.delete(producto)
            db.session.commit()
            return Producto
        return None
    
    def save(self, entity: Producto) -> Producto:
        db.session.add(entity) 
        db.session.commit()
        return entity
     