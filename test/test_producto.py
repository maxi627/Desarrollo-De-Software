import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app
from app.models.producto import Producto

class ProductoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_Producto(self):
        object=Producto()
        object.id_producto = '1'
        object.nombre = 'Nombre'
        object.precio="123"
        object.stock="23"
        self.assertTrue(object.id_producto, '1')
        self.assertTrue(object.nombre, 'Nombre')
        self.assertTrue(object.precio, '123')
        self.assertTrue(object.stock, '23')

if __name__ == '__main__':
    unittest.main()