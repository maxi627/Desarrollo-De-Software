from marshmallow import fields, Schema, post_load
from app.models import like

# Esquema para el modelo Like
class LikeSchema(Schema):
    id = fields.Integer(dump_only=True)
    post_id = fields.Integer(required=True)
    usuario_id = fields.Integer(required=True)

    @post_load
    def make_like(self, data, **kwargs):
        return like(**data)

