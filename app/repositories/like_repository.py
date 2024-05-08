from app.models import Like
from app import db

class LikeRepository:
    def __init__(self):
        self.__model = Like

    def get_all(self) -> list[Like]:
        return db.session.query(self.__model).all()

    def get_by_id(self, id) -> Like:
        return db.session.query(self.__model).get(id)

    def create(self, entity: Like) -> Like:
        db.session.add(entity)
        db.session.commit()
        return entity

    def update(self, id, t: Like) -> Like:
        entity = self.get_by_id(id)
        if entity:
            entity.post_id= t.post_id
            db.session.add(entity)
            db.session.commit()
            return entity
        return None

    def delete(self, id)-> bool:
        like = self.get_by_id(id)
        if like:
            db.session.delete(like)
            db.session.commit()
            return like
        return None