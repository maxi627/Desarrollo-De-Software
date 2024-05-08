

from app.models import Post
from app import db

class PostRepository:
    def __init__(self):
        self.__model = Post 
        
    def get_all(self) -> list[Post]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Post:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Post) -> Post:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Post) -> Post:
        entity = self.get_by_id(id)  
        if entity:
            entity.contenido=t.contenido
            entity.fecha_creacion=t.fecha_creacion
            entity.autor=t.autor
            entity.autor_id=t.autor_id
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id) -> bool:
        post = self.get_by_id(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return post
        return None