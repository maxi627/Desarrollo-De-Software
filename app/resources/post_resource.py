from flask import jsonify, Blueprint, request
from app.mapping import PostSchema
from app.services import PostService

post = Blueprint('post', __name__)
service = PostService()
post_schema = PostSchema()

"""
Obtiene todas las posts
"""
@post.route('/posts', methods=['GET'])
def all():
    resp = post_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una post por id
"""
@post.route('/posts/<int:id>', methods=['GET'])
def one(id):
    resp = post_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva post
"""
@post.route('/posts', methods=['POST'])
def create():
    post = post_schema.load(request.json)
    resp = post_schema.dump(service.create(post))
    return resp, 201

"""
Actualiza una post existente
"""
@post.route('/posts/<int:id>', methods=['PUT'])
def update(id):
    post = post_schema.load(request.json)
    resp = post_schema.dump(service.update(id, post))
    return resp, 200

"""
Elimina una post existente
"""
@post.route('/posts/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "post eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el post"
    return jsonify(msg), 204