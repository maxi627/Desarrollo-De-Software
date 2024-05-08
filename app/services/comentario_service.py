
from app.models import Comentario
from app.repositories import ComentarioRepository


class ComentarioService:
    def __init__(self):
        self.repository = ComentarioRepository()

    def get_all(self) -> list[Comentario]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Comentario:
        return self.repository.get_by_id(id)

    def create(self, entity: Comentario)-> Comentario:
        return self.repository.create(entity)

    def update(self, id, Comentario) -> Comentario:
        return self.repository.update(id, Comentario)

    def delete(self, id)->bool:
        return self.repository.delete(id)