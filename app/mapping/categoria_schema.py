
from marshmallow import fields, Schema, post_load,validate
from app.models.orden import Categoria
# Esquema para el modelo Categoria:
class CategoriaSchema(Schema):
    id_categoria = fields.Integer(dump_only=True)
    nombre = fields.String(required=True,validate=validate.Length(min=2, max=40))

    @post_load
    def make_categoria(self, data, **kwargs):
        return Categoria(**data)