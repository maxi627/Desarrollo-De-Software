from marshmallow import fields, Schema, post_load
from app.models.producto import Producto

class ProductoSchema(Schema):
    id_producto = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    precio = fields.Integer(required=True)
    stock = fields.Integer(required=True)
    id_categoria = fields.Integer(required=True)
    
    categoria = fields.Nested("CategoriaSchema", many=False, only=("id_categoria", "nombre"))
    
    @post_load
    def make_producto(self, data, **kwargs):
        return Producto(**data)
