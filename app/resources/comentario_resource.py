from flask import jsonify, Blueprint, request
from app.mapping import ComentarioSchema
from app.services import ComentarioService

comentario = Blueprint('comentario', __name__)
service = ComentarioService()
comentario_schema = ComentarioSchema()

"""
Obtiene todas las comentarios
"""
@comentario.route('/comentarios', methods=['GET'])
def all():
    resp = comentario_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene un comentario por id
"""
@comentario.route('/comentarios/<int:id>', methods=['GET'])
def one(id):
    resp = comentario_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea un nuevo comentario
"""
@comentario.route('/comentarios', methods=['POST'])
def create():
    comentario = comentario_schema.load(request.json)
    resp = comentario_schema.dump(service.create(comentario))
    return resp, 201

"""
Actualiza un comentario existente
"""
@comentario.route('/comentarios/<int:id>', methods=['PUT'])
def update(id):
    comentario = comentario_schema.load(request.json)
    resp = comentario_schema.dump(service.update(id, comentario))
    return resp, 200

"""
Elimina un comentario existente
"""
@comentario.route('/comentarios/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "comentario eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el comentario"
    return jsonify(msg), 204