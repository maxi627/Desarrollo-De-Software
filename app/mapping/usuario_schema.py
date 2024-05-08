from marshmallow import validate, Schema, fields, post_load
from app.models import Usuario

# Define el esquema (Schema) para la clase Usuario
class UsuarioSchema(Schema):
    # Define campos del esquema y establece reglas de validación y serialización

    id = fields.Integer(dump_only=True)  # Campo 'id' de tipo Integer (solo para volcado/serialización)
    nombre = fields.String(required=True, validate=validate.Length(min=2, max=120))  # Campo 'nombre' de tipo String obligatorio con validación de longitud
    email = fields.String(required=True, validate=validate.Email())  # Campo 'email' de tipo String obligatorio con validación de email
    contrasena = fields.String(load_only=True)  # Campo 'contrasena' de tipo String (solo para carga/deserialización)

    # Método para manejar la carga de datos (deserialización)
    @post_load
    def make_usuario(self, data, **kwargs):
        return Usuario(**data)  # Crea una instancia de la clase Usuario con los datos deserializados
