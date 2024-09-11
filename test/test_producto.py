import unittest
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from flask import current_app
from app import create_app,db
from app.models.producto import Producto
from app.services.producto_service import ProductoService
producto_service=ProductoService()

class ProductoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.id_producto = 1
        self.nombre = "Nombre"
        self.precio = 123
        self.stock = 23
        # self.id_categoria=1
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def __get_producto(self):
        return Producto(
            id_producto=self.id_producto,
            nombre=self.nombre,
            precio=self.precio,
            stock=self.stock,
            # id_categoria=self.id_categoria

        )

    def test_producto_save(self):
        producto = self.__get_producto()
        producto_service.save(producto)
        producto_find = producto_service.get_by_id(producto.id_producto)
        print(f"Producto guardado: {producto_find}")
        self.assertEqual(producto.id_producto, self.id_producto)
        self.assertEqual(producto.nombre, self.nombre)
        self.assertEqual(producto.precio, self.precio)
        self.assertEqual(producto.stock, self.stock)


    def test_producto_delete(self):
        producto = self.__get_producto()
        producto_service.save(producto)
        self.assertIsNotNone(producto_service.get_by_id(producto.id_producto))  # Asegura que el producto fue guardado
        producto_service.delete(producto.id_producto)
        self.assertIsNone(producto_service.get_by_id(producto.id_producto))

    def test_producto_all(self):
        producto = self.__get_producto()
        producto_service.save(producto)
        productos = producto_service.get_all()
        self.assertGreaterEqual(len(productos), 1) 

    def test_producto_find(self):
        producto = self.__get_producto()
        producto_service.save(producto)
        producto_find = producto_service.get_by_id(producto.id_producto)  # Debe devolver un objeto Producto
        self.assertIsNotNone(producto_find)  # Verifica que el producto fue encontrado
        self.assertEqual(producto_find.id_producto, producto.id_producto)
        self.assertEqual(producto_find.nombre, producto.nombre)
        self.assertEqual(producto_find.precio, producto.precio)
        self.assertEqual(producto_find.stock, producto.stock)


if __name__ == '__main__':
    unittest.main()