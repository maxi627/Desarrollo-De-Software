import unittest
from flask import current_app
from app import create_app, db
from app.models import User
from app.services import PassLibSecurity
from app.services.usuario_service import UserService

user_service = UserService()

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.id_user = 1
        self.nombre = 'nombre'
        self.email = "123@gmail.com"
        self.password = "67"

    def __get_user(self):
        return User(
            id_user=self.id_user,
            nombre=self.nombre,
            email=self.email,
            password=self.password
        )

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def __recargar(self, id):
        """Descarta lo que hay en la sesión y vuelve a leer el usuario de la base."""
        db.session.expire_all()
        return user_service.get_by_id(id)

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_user_save(self):
        user = self.__get_user()
        user_service.save(user)
        self.assertEqual(user.id_user, self.id_user)
        self.assertEqual(user.nombre, self.nombre)
        self.assertEqual(user.email, self.email)

    def test_user_save_guarda_password_hasheada(self):
        user_service.save(self.__get_user())
        user_db = self.__recargar(self.id_user)
        self.assertIsNotNone(user_db.password)               # se persiste en la base
        self.assertNotEqual(user_db.password, self.password)  # nunca en texto plano

    def test_user_delete(self):
        user = self.__get_user()
        user_service.save(user)
        self.assertTrue(user_service.delete(user.id_user))
        self.assertIsNone(user_service.get_by_id(user.id_user))

    def test_user_delete_inexistente(self):
        self.assertFalse(user_service.delete(999))

    def test_user_all(self):
        user = self.__get_user()
        user_service.save(user)
        users = user_service.get_all()
        self.assertGreaterEqual(len(users), 1)

    def test_user_find(self):
        user = self.__get_user()
        user_service.save(user)
        user_find = user_service.get_by_id(1)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id_user, user.id_user)
        self.assertEqual(user_find.email, user.email)

    def test_find_by_email(self):
        user_service.save(self.__get_user())
        self.assertEqual(user_service.find_by_email(self.email).id_user, self.id_user)
        self.assertIsNone(user_service.find_by_email("otro@gmail.com"))

    def test_check_auth(self):
        user_service.save(self.__get_user())
        self.assertTrue(user_service.check_auth(self.email, self.password))
        self.assertFalse(user_service.check_auth(self.email, "incorrecta"))
        self.assertFalse(user_service.check_auth("otro@gmail.com", self.password))

    def test_user_update_conserva_password_si_no_se_envia(self):
        user_service.save(self.__get_user())
        cambios = User(nombre="otro nombre", email=self.email, password=None)
        user_service.update(self.id_user, cambios)
        user_db = self.__recargar(self.id_user)
        self.assertEqual(user_db.nombre, "otro nombre")
        self.assertTrue(user_service.check_auth(self.email, self.password))

    def test_user_update_cambia_password(self):
        user_service.save(self.__get_user())
        cambios = User(nombre=self.nombre, email=self.email, password="nueva")
        user_service.update(self.id_user, cambios)
        self.__recargar(self.id_user)
        self.assertTrue(user_service.check_auth(self.email, "nueva"))
        self.assertFalse(user_service.check_auth(self.email, self.password))

    def test_passlib_intercambiable(self):
        """Liskov: con PassLibSecurity el servicio funciona igual que con Werkzeug."""
        service = UserService(PassLibSecurity())
        service.save(self.__get_user())
        user_db = self.__recargar(self.id_user)
        self.assertTrue(user_db.password.startswith("$pbkdf2-sha256$"))
        self.assertTrue(service.check_auth(self.email, self.password))
        self.assertFalse(service.check_auth(self.email, "incorrecta"))

    def test_endpoint_crear_usuario(self):
        client = self.app.test_client()
        resp = client.post('/api/v1/Users', json={
            "nombre": self.nombre, "email": self.email, "password": self.password
        })
        self.assertEqual(resp.status_code, 201)
        self.assertNotIn("password", resp.get_json())  # la contraseña nunca se devuelve
        id_user = resp.get_json()["id_user"]

        resp = client.get(f'/api/v1/Users/{id_user}')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["email"], self.email)
        self.assertTrue(user_service.check_auth(self.email, self.password))


if __name__ == '__main__':
    unittest.main()
