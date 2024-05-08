
from marshmallow import fields, Schema, post_load,validate
from app.models.post import Post
# Esquema para el modelo Post
class PostSchema(Schema):
    id = fields.Integer(dump_only=True)
    titulo = fields.String(required=True,validate=validate.Length(min=2, max=40))
    contenido = fields.String(required=True,validate=validate.Length(min=2, max=160))
    fecha_creacion = fields.DateTime(dump_only=True)
    autor = fields.Nested("UsuarioSchema", many=True, only=("id", "nombre", "email"))

    @post_load
    def make_post(self, data, **kwargs):
        return Post(**data)