from app.models import Orden  # Importa el modelo Orden desde app.models
from app import db  

class OrdenRepository:
    def __init__(self):
        self.__model = Orden  # Inicializa el modelo Orden en el repositorio

    # Método para obtener todas las órdenes
    def get_all(self) -> list[Orden]:
        return db.session.query(self.__model).all()

    # Método para obtener una orden por su ID
    def get_by_id(self, id) -> Orden:
        return db.session.query(self.__model).get(id)

    # Método para crear una nueva orden
    def create(self, entity: Orden) -> Orden:
        db.session.add(entity)
        db.session.commit()
        return entity

    # Método para actualizar una orden existente
    def update(self, id, t: Orden) -> Orden:
        entity = self.get_by_id(id)  # Obtiene la orden por su ID
        if entity:
            # Actualiza los atributos de la orden con los valores del objeto t
            entity.id_producto = t.id_producto
            entity.cantidad = t.cantidad
            entity.precio = t.precio
            entity.id_pedido = t.id_pedido
            entity.id_detalle=t.id_detalle
            db.session.add(entity)  # Agrega la orden actualizada a la sesión
            db.session.commit()  # Guarda los cambios en la base de datos
            return entity  # Retorna la orden actualizada
        return None  # Retorna None si no se encuentra la orden

    # Método para eliminar una orden por su ID
    def delete(self, id) -> bool:
        orden = self.get_by_id(id)  # Obtiene la orden por su ID
        if orden:
            db.session.delete(orden)  # Elimina la orden de la sesión
            db.session.commit()  # Guarda los cambios en la base de datos
            return orden  # Retorna la orden eliminada
        return None  # Retorna None si no se encuentra la orden
