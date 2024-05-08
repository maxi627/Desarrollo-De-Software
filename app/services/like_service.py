
from app.models import Like
from app.repositories import LikeRepository


class LikeService:
    def __init__(self):
        self.repository = LikeRepository()

    def get_all(self) -> list[Like]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Like:
        return self.repository.get_by_id(id)

    def create(self, entity: Like)-> Like:
        return self.repository.create(entity)

    def update(self, id, Like) -> Like:
        return self.repository.update(id, Like)

    def delete(self, id)->bool:
        return self.repository.delete(id)