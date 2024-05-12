from flask import jsonify, Blueprint, request
from app.mapping import OrdenSchema
from app.services import OrdenService

orden = Blueprint('orden', __name__)
service = OrdenService()
orden_schema = OrdenSchema()

"""
Obtiene todas las orden
"""
@orden.route('/orden', methods=['GET'])
def all():
    resp = orden_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una orden por id
"""
@orden.route('/orden/<int:id>', methods=['GET'])
def one(id):
    resp = orden_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva orden
"""
@orden.route('/orden', methods=['POST'])
def create():
    orden = orden_schema.load(request.json)
    resp = orden_schema.dump(service.create(orden))
    return resp, 201

"""
Actualiza una orden existente
"""
@orden.route('/orden/<int:id>', methods=['PUT'])
def update(id):
    orden = orden_schema.load(request.json)
    resp = orden_schema.dump(service.update(id, orden))
    return resp, 200

"""
Elimina una orden existente
"""
@orden.route('/orden/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "orden eliminada correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el orden"
    return jsonify(msg), 204