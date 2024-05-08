from flask import jsonify, Blueprint, request
from app.mapping import LikeSchema
from app.services import LikeService

like = Blueprint('like', __name__)
service = LikeService()
like_schema = LikeSchema()

"""
Obtiene todos las likes
"""
@like.route('/likes', methods=['GET'])
def all():
    resp = like_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una like por id
"""
@like.route('/likes/<int:id>', methods=['GET'])
def one(id):
    resp = like_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva like
"""
@like.route('/likes', methods=['POST'])
def create():
    like = like_schema.load(request.json)
    resp = like_schema.dump(service.create(like))
    return resp, 201

"""
Actualiza una like existente
"""
@like.route('/likes/<int:id>', methods=['PUT'])
def update(id):
    like = like_schema.load(request.json)
    resp = like_schema.dump(service.update(id, like))
    return resp, 200

"""
Elimina una like existente
"""
@like.route('/likes/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Like eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el Like"
    return jsonify(msg), 204