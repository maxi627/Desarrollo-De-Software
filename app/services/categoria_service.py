
from app.models import Categoria
from app.repositories import CategoriaRepository


class CategoriaService:
    def __init__(self):
        self.repository = CategoriaRepository()

    def get_all(self) -> list[Categoria]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Categoria:
        return self.repository.get_by_id(id)

    def create(self, entity: Categoria)-> Categoria:
        return self.repository.create(entity)

    def update(self, id, Categoria) -> Categoria:
        return self.repository.update(id, Categoria)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Categoria) -> Categoria:
        return self.repository.save(entity)
     