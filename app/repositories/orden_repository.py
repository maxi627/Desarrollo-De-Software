from app.models import Orden  
from app import db  
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save



class OrdenRepository(Repository_get,Repository_create,Repository_delete,Repository_update,Repository_save):
    def __init__(self):
        self.__model = Orden  

    def get_all(self) -> list[Orden]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Orden:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Orden) -> Orden:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Orden) -> Orden:
        entity = self.get_by_id(id)  
        if entity:
            
            entity.id_producto = t.id_producto
            entity.cantidad = t.cantidad
            entity.precio = t.precio
            entity.id_pedido = t.id_pedido
            entity.id_detalle=t.id_detalle
            db.session.add(entity)  
            db.session.commit() 
            return entity 
        return None 

   
    def delete(self, id) -> bool:
        orden = self.get_by_id(id)  
        if orden:
            db.session.delete(orden) 
            db.session.commit()  
            return orden  
        return None  
    def save(self, entity: Orden) -> Orden:
        db.session.add(entity) 
        db.session.commit()
        return entity
         