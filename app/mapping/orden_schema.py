from marshmallow import fields, Schema, post_load
from app.models.orden import Orden

# Esquema para el modelo Orden:
class OrdenSchema(Schema):
    id_detalle = fields.Integer(dump_only=True)
    id_pedido = fields.Integer(required=True)
    id_producto = fields.Integer(required=True)
    cantidad = fields.Integer(required=True)
    precio = fields.Integer(required=True)

    @post_load
    def make_orden(self, data, **kwargs):
        return Orden(**data)
