from app.models import User
from app import db
from .repository import Repository_get, Repository_create, Repository_update, Repository_delete,Repository_save


class UserRepository(Repository_save,Repository_get,Repository_create,Repository_update,Repository_delete):  
     def __init__(self):
         self.__model = User

     def get_all(self) -> list[User]:
        try:
            return db.session.query(self.__model).all()
        except Exception as e:
            print(f"error al buscar los Users {e}")
            return []
        
     def get_by_id(self, id) -> User:
         return db.session.query(self.__model).get(id)
     
     
     def create(self, entity: User) -> User:
         db.session.add(entity)
         db.session.commit()
         return entity
     
     
     def update(self, id, t: User) -> User:
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
         User = self.get_by_id(id)
         if User:
             db.session.delete(User)
             db.session.commit()
             return True
         return False
     def save(self, entity: User) -> User:
        db.session.add(entity) 
        db.session.commit()
        return entity
     