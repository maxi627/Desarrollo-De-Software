
    # CAPAZ SIRVE PARA PONER EN SERVICE
    # def search(self, criteria):
    #     """
    #     Busca comentarios basados en criterios específicos.

    #     Args:
    #     - criteria (dict): Diccionario con los criterios de búsqueda.

    #     Returns:
    #     - comentarios (List[Producto]): Lista de comentarios que coinciden con los criterios.
    #     """
    #     return Producto.query.filter_by(**criteria).all()

from app.models import Producto
from app import db

class ProductoRepository:
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