
    # CAPAZ SIRVE PARA PONER EN SERVICE
    # def search(self, criteria):
    #     """
    #     Busca comentarios basados en criterios específicos.

    #     Args:
    #     - criteria (dict): Diccionario con los criterios de búsqueda.

    #     Returns:
    #     - comentarios (List[Comentario]): Lista de comentarios que coinciden con los criterios.
    #     """
    #     return Comentario.query.filter_by(**criteria).all()

from app.models import Comentario
from app import db

class ComentarioRepository:
    def __init__(self):
        self.__model = Comentario 
        
    def get_all(self) -> list[Comentario]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Comentario:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Comentario) -> Comentario:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Comentario) -> Comentario:
        entity = self.get_by_id(id) 
        if entity: 
            entity.contenido=t.contenido
            entity.fecha_creacion=t.fecha_creacion
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        comentario = self.get_by_id(id) 
        if comentario: 
            db.session.delete(comentario)
            db.session.commit()
            return Comentario
        return None