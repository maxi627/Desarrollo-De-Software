
from app.models import Orden
from app.repositories import OrdenRepository


class OrdenService:
    def __init__(self):
        self.repository = OrdenRepository()

    def get_all(self) -> list[Orden]:
        return self.repository.get_all()

    def get_by_id(self, id)-> Orden:
        return self.repository.get_by_id(id)

    def create(self, entity: Orden)-> Orden:
        return self.repository.create(entity)

    def update(self, id, Orden) -> Orden:
        return self.repository.update(id, Orden)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Orden) -> Orden:
        return self.repository.save(entity)
     