from flask import jsonify, Blueprint, request
from app.mapping import UsuarioSchema
from app.services import UsuarioService

usuario = Blueprint('usuario', __name__)
service = UsuarioService()
usuario_schema = UsuarioSchema()

"""
Obtiene todos las usuarios
"""
@usuario.route('/usuarios', methods=['GET'])
def all():
    resp = usuario_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
filtra los usuarios por su inicial
"""
@usuario.route('/usuarios_inicial/<string:inicial>', methods=['GET'])
def all_inv(inicial):
    resp = usuario_schema.dump(service.get_all_inicial(inicial), many=True) 
    return resp, 200

"""
Obtiene una usuario por id
"""
@usuario.route('/usuarios/<int:id>', methods=['GET'])
def one(id):
    resp = usuario_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva usuario
"""
@usuario.route('/usuarios', methods=['POST'])
def create():
    usuario = usuario_schema.load(request.json)
    resp = usuario_schema.dump(service.create(usuario))
    return resp, 201

"""
Actualiza una usuario existente
"""
@usuario.route('/usuarios/<int:id>', methods=['PUT'])
def update(id):
    usuario = usuario_schema.load(request.json)
    resp = usuario_schema.dump(service.update(id, usuario))
    return resp, 200

"""
Elimina un usuario existente
"""
@usuario.route('/usuarios/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "usuario eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el usuario"
    return jsonify(msg), 204