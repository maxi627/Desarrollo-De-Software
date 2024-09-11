import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app, db
from app.models.usuario import Usuario
from app.services.usuario_service import UsuarioService

user_service = UsuarioService()

class UsuarioTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.id_usuario = 1
        self.nombre = 'nombre'
        self.email = "123@gmail.com"
        self.password = "67"
    
    def __get_user(self):
        return Usuario(
            id_usuario=self.id_usuario,
            nombre=self.nombre,
            email=self.email,
            password=self.password
        )
            
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
        

    def test_user_save(self):
        user = self.__get_user()
        user_service.save(user)
        self.assertEqual(user.id_usuario, self.id_usuario)
        self.assertEqual(user.nombre, self.nombre)
        self.assertEqual(user.email, self.email)
        
    def test_user_delete(self):
        user = self.__get_user()
        user_service.save(user)
        user_service.delete(user.id_usuario)
        self.assertIsNone(user_service.get_by_id(user.id_usuario))
        
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
        self.assertEqual(user_find.id_usuario, user.id_usuario)
        self.assertEqual(user_find.email, user.email)



if __name__ == '__main__':
    unittest.main()
