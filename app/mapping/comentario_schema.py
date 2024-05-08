from marshmallow import fields, Schema, post_load
from app.models.comentario import Comentario

# Esquema para el modelo Comentario
class ComentarioSchema(Schema):
    id = fields.Integer(dump_only=True)
    contenido = fields.String(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    autor = fields.Nested("UsuarioSchema", only=("id", "nombre", "email"))
    post = fields.Nested("PostSchema", many=True, only=("id", "titulo"))

    @post_load
    def make_comentario(self, data, **kwargs):
        return Comentario(**data)
    