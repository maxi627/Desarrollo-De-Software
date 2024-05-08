
from marshmallow import fields, Schema, post_load,validate
from app.models.categorias import Categoria
# Esquema para el modelo Categoria:
class CategoriaSchema(Schema):
    id_categoria = fields.Integer(dump_only=True)
    nombre = fields.String(required=True,validate=validate.Length(min=2, max=40))
    productos = fields.Nested("ProductoSchema", many=True, only=("id_producto", "nombre", "precio", "stock"))
    
    @post_load
    def make_categoria(self, data, **kwargs):
        return Categoria(**data)