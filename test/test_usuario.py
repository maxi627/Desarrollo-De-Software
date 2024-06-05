import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app, db
from app.models.usuario import Usuario

class UsuarioTestCase(unittest.TestCase):
    """
    Test User model
    Aplicando principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
    """

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.id_usuario = 1
        self.nombre = 'nombre'
        self.email = "123@gmail.com"
        self.password = "67"
    

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
        
    def test_user(self):
        user = self.__get_user()
        self.assertEqual(user.id_usuario, self.id_usuario)
        self.assertEqual(user.nombre, self.nombre)
        self.assertEqual(user.email, self.email)

        
    def test_user_save(self):
        user = self.__get_user()
        db.session.add(user)
        db.session.commit()
    
        self.assertEqual(user.id_usuario, self.id_usuario)
        self.assertEqual(user.nombre, self.nombre)
        self.assertEqual(user.email, self.email)
        
    def test_user_delete(self):
        user = self.__get_user()
        db.session.add(user)
        db.session.commit()

        # Borrar el usuario
        db.session.delete(user)
        db.session.commit()
        
        self.assertIsNone(Usuario.query.get(user.id_usuario))
        
    def test_user_all(self):
        user = self.__get_user()
        db.session.add(user)
        db.session.commit()

        users = Usuario.query.all()
        self.assertGreaterEqual(len(users), 1)
    
    def test_user_find(self):
        user = self.__get_user()
        db.session.add(user)
        db.session.commit()

        user_find = Usuario.query.get(self.id_usuario)
        self.assertIsNotNone(user_find)
        self.assertEqual(user_find.id_usuario, user.id_usuario)
        self.assertEqual(user_find.email, user.email)

    def __get_user(self):
        return Usuario(
            id_usuario=self.id_usuario,
            nombre=self.nombre,
            email=self.email,
            password=self.password,
        )

if __name__ == '__main__':
    unittest.main()
