import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app, db
from app.models.User import User
from app.services.User_service import UserService

user_service = UserService()

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.id_User = 1
        self.nombre = 'nombre'
        self.email = "123@gmail.com"
        self.password = "67"
    
    def __get_user(self):
        return User(
            id_User=self.id_User,
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
        self.assertEqual(user.id_User, self.id_User)
        self.assertEqual(user.nombre, self.nombre)
        self.assertEqual(user.email, self.email)
        
    def test_user_delete(self):
        user = self.__get_user()
        user_service.save(user)
        user_service.delete(user.id_User)
        self.assertIsNone(user_service.get_by_id(user.id_User))
        
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
        self.assertEqual(user_find.id_User, user.id_User)
        self.assertEqual(user_find.email, user.email)



if __name__ == '__main__':
    unittest.main()
