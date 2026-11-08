from marshmallow import validate, Schema, fields, post_load
from app.models import User

# Define el esquema (Schema) para la clase User
class UserSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id_user = fields.Integer(dump_only=True)  # Solo para volcado/serialización
    nombre = fields.String(required=True, validate=validate.Length(min=2, max=120))
    email = fields.String(required=True, validate=validate.Email())
    id_detalle = fields.Integer(allow_none=True)  # Detalle de orden asociado (opcional)
    password = fields.String(required=True, load_only=True)  # Solo para carga: nunca se devuelve

    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_User(self, data, **kwargs):
        return User(**data)  # Crea una instancia de la clase User con los datos deserializados
