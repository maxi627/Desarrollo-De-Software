from flask import jsonify, Blueprint, request
from app.mapping import UserSchema
from app.services import UserService

user = Blueprint('User', __name__)
service = UserService()
user_schema = UserSchema()

"""
Obtiene todos las Users
"""
@user.route('/Users', methods=['GET'])
def all():
    resp = user_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
filtra los Users por su inicial
"""
@user.route('/Users_inicial/<string:inicial>', methods=['GET'])
def all_inv(inicial):
    resp =user_schema.dump(service.get_all_inicial(inicial), many=True) 
    return resp, 200

"""
Obtiene una User por id
"""
@user.route('/Users/<int:id>', methods=['GET'])
def one(id):
    resp = user_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva User
"""
@user.route('/Users', methods=['POST'])
def create():
    User = user_schema.load(request.json)
    resp = user_schema.dump(service.create(User))
    return resp, 201

"""
Actualiza una User existente
"""
@user.route('/Users/<int:id>', methods=['PUT'])
def update(id):
    User = user_schema.load(request.json)
    resp = user_schema.dump(service.update(id, User))
    return resp, 200

"""
Elimina un User existente
"""
@user.route('/Users/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "User eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el User"
    return jsonify(msg), 204