
from app.models import Usuario
from app.repositories import UsuarioRepository


class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def get_all(self) -> list[Usuario]:
        users= self.repository.get_all()
        return list(users)
    
    def get_all_inicial(self, inicial) -> list[Usuario]:
        users = self.repository.get_all()
        return [x for x in users if x.nombre[0].lower()==inicial.lower()]
    
    def get_by_id(self, id)-> Usuario:
        return self.repository.get_by_id(id)

    def create(self, entity: Usuario)-> Usuario:
        return self.repository.create(entity)

    def update(self, id, Usuario) -> Usuario:
        return self.repository.update(id, Usuario)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    
    def save(self, entity: Usuario) -> Usuario:
        return self.repository.save(entity)
     