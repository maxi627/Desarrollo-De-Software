from app.models import Usuario
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class UsuarioRepository(Repository_save,Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = Usuario

     def get_all(self) -> list[Usuario]:
        try:
            return db.session.query(self.__model).all()
        except Exception as e:
            print(f"error al buscar los usuarios {e}")
            return []
        
     def get_by_id(self, id) -> Usuario:
         return db.session.query(self.__model).get(id)
     
     
     def create(self, entity: Usuario) -> Usuario:
         db.session.add(entity)
         db.session.commit()
         return entity
     
     
     def update(self, id, t: Usuario) -> Usuario:
         entity = self.get_by_id(id)
         if entity:
             entity.password=t.password
             entity.email=t.email
             entity.nombre=t.nombre
             entity.id_pedido=t.id_pedido
             db.session.add(entity)
             db.session.commit()
             return entity
         return None
     
     
     def delete(self, id)-> bool:
         usuario = self.get_by_id(id)
         if usuario:
             db.session.delete(usuario)
             db.session.commit()
             return True
         return False
     def save(self, entity: Usuario) -> Usuario:
        db.session.add(entity) 
        db.session.commit()
        return entity
     