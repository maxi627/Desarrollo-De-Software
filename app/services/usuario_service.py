
from app.models import User
from app.repositories import UserRepository
repository=UserRepository()


class UserService:
    def __init__(self):
        from app.services import SecurityManager, WerkzeugSecurity
        self.__security = SecurityManager(WerkzeugSecurity())
        
    def save(self, entity: User) -> User:
        entity.password=self.__security.generate_password(entity.password)
        return self.__security.save(entity)

    def update(self, id, user) -> User:
        if user.password is not None:
            user.password=self.__security.generate_password(user.password)
        return repository.update(id, user)

    def delete(self, id)->bool:
        user=repository.get_by_id(id)
        return repository.delete(user)
    
    def get_all(self) -> list[User]:
        users= repository.get_all()
        return list(users)
    
    def get_all_inicial(self, inicial) -> list[User]:
        users = repository.get_all()
        return [x for x in users if x.nombre[0].lower()==inicial.lower()]
    
    def get_by_id(self, id)-> User:
        return repository.get_by_id(id)

    def create(self, entity: User)-> User:
        return repository.create(entity)

    def check_auth(self, username, password) -> bool:
        user = self.find_by_username(username)
        if user is not None:
            return self.__security.check_password(user.password, password)
        else:
            return False
        

     