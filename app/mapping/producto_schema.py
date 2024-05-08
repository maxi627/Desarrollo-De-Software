from marshmallow import fields, Schema, post_load
from app.models.producto import Producto

# Esquema para el modelo Producto:
class ProductoSchema(Schema):
    id_producto = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    precio = fields.Integer(dump_only=True)
    stock = fields.Integer(dump_only=True)
    id_categoria = fields.Nested("PostCategorias", many=True, only=(""))

    @post_load
    def make_producto(self, data, **kwargs):
        return Producto(**data)
    