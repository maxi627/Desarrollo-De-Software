from marshmallow import validate, Schema, fields, post_load
from app.models import User

# Define el esquema (Schema) para la clase User
class UserSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    nombre = fields.String(required=True, validate=validate.Length(min=2, max=120))  
    email = fields.String(required=True, validate=validate.Email()) 
    id_pedido = fields.Int(required=True)
    password = fields.String(load_only=True)  # Campo 'password' de tipo String (solo para carga/deserialización)

    User= fields.Nested("OrdenSchema", many=True, only=("id_detalle","id_pedido","id_producto","cantidad","precio"))
    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_User(self, data, **kwargs):
        return User(**data)  # Crea una instancia de la clase User con los datos deserializados
