import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app,db
from app.models.orden import Orden
from app.services.orden_service import OrdenService

orden_service=OrdenService()
class OrdenTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.id_detalle=1
        self.id_producto=2
        self.cantidad=3
        self.precio=4
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def __get_orden(self):
        return Orden(
            id_detalle=self.id_detalle,
            # id_producto=self.id_producto,
            cantidad=self.cantidad,
            precio=self.precio
        )

    def test_orden_save(self):
        orden=self.__get_orden()
        orden_service.save(orden)
        self.assertEqual(orden.id_detalle, 1)
        # self.assertEqual(orden.id_producto, '2')
        self.assertEqual(orden.cantidad, 3)
        self.assertEqual(orden.precio, 4)

    def test_orden_delete(self):
        orden=self.__get_orden()
        orden_service.save(orden)
        self.assertIsNotNone(orden_service.get_by_id(orden.id_detalle))
        orden_service.delete(orden.id_detalle)
        self.assertIsNone(orden_service.get_by_id(orden.id_detalle))
    
    def test_orden_all(self):
        orden=self.__get_orden()
        orden_service.save(orden)
        ordenes=orden_service.get_all()
        self.assertGreaterEqual(len(ordenes),1)
        
    def test_orden_find(self):
        orden=self.__get_orden()
        orden_service.save(orden)
        orden_find=orden_service.get_by_id(orden.id_detalle)
        self.assertIsNotNone(orden_find) 
        # self.assertEqual(orden_find.id_producto,orden.id_producto)
        self.assertEqual(orden_find.id_detalle,orden.id_detalle)
        self.assertEqual(orden_find.cantidad,orden.cantidad)
        self.assertEqual(orden_find.precio,orden.precio)   
if __name__ == '__main__':
    unittest.main()