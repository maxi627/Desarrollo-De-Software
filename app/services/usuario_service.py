
from app.models import User
from app.repositories import UserRepository
repository=UserRepository()


class UserService:
    def __init__(self, security=None):
        """
        security: implementación de AbstractSecurity (WerkzeugSecurity por defecto).
        Se puede pasar PassLibSecurity sin cambiar nada más (Liskov / inversión de dependencias).
        """
        from app.services import SecurityManager, WerkzeugSecurity
        self.__security = SecurityManager(security or WerkzeugSecurity())

    def save(self, entity: User) -> User:
        """Guarda un usuario nuevo con la contraseña hasheada."""
        entity.password=self.__security.generate_password(entity.password)
        return repository.save(entity)

    def update(self, id, user) -> User:
        if user.password is not None:
            user.password=self.__security.generate_password(user.password)
        return repository.update(id, user)

    def delete(self, id)->bool:
        return repository.delete(id)

    def get_all(self) -> list[User]:
        users= repository.get_all()
        return list(users)

    def get_all_inicial(self, inicial) -> list[User]:
        users = repository.get_all()
        return [x for x in users if x.nombre[0].lower()==inicial.lower()]

    def get_by_id(self, id)-> User:
        return repository.get_by_id(id)

    def find_by_email(self, email) -> User:
        return repository.get_by_email(email)

    def create(self, entity: User)-> User:
        # Mismo comportamiento que save: nunca se guarda la contraseña en texto plano.
        return self.save(entity)

    def check_auth(self, email, password) -> bool:
        """Verifica las credenciales de un usuario (se identifica por su email)."""
        user = self.find_by_email(email)
        if user is not None:
            return self.__security.check_password(user.password, password)
        else:
            return False
