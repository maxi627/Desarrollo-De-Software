import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app
from app.models.orden import Orden

class OrdenTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_Orden(self):
        object=Orden()
        object.id_detalle = '1'
        object.id_producto="123"
        object.cantidad="67"
        object.precio="34"
        self.assertTrue(object.id_detalle, '1')
        self.assertTrue(object.id_producto, '123')
        self.assertTrue(object.cantidad, '67')
        self.assertTrue(object.precio, '34')

if __name__ == '__main__':
    unittest.main()