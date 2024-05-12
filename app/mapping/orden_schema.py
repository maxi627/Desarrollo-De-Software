from marshmallow import fields, Schema, post_load
from app.models.orden import Orden

# Esquema para el modelo Orden:
class OrdenSchema(Schema):
    id_detalle = fields.Integer(dump_only=True)
    id_pedido = fields.Integer(required=True)
    id_producto = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)
    precio = fields.Integer(required=True)
    producto = fields.Nested("ProductoSchema", many=False, only=("id_producto", "nombre", "precio", "stock"))

    
    @post_load
    def make_orden(self, data, **kwargs):
        return Orden(**data)
