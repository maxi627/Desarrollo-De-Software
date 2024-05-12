from flask import jsonify, Blueprint, request
from app.mapping import ProductoSchema
from app.services import ProductoService

producto = Blueprint('producto', __name__)
service = ProductoService()
producto_schema = ProductoSchema()

"""
Obtiene todos las productos
"""
@producto.route('/productos', methods=['GET'])
def all():
    resp = producto_schema.dump(service.get_all(), many=True) 
    return resp, 200

"""
Obtiene una producto por id
"""
@producto.route('/productos/<int:id>', methods=['GET'])
def one(id):
    resp = producto_schema.dump(service.get_by_id(id)) 
    return resp, 200

"""
Crea nueva producto
"""
@producto.route('/productos', methods=['POST'])
def create():
    producto = producto_schema.load(request.json)
    resp = producto_schema.dump(service.create(producto))
    return resp, 201

"""
Actualiza una producto existente
"""
@producto.route('/productos/<int:id>', methods=['PUT'])
def update(id):
    producto = producto_schema.load(request.json)
    resp = producto_schema.dump(service.update(id, producto))
    return resp, 200

"""
Elimina una producto existente
"""
@producto.route('/productos/<int:id>', methods=['DELETE'])
def delete(id):
    msg = "Producto eliminado correctamente"
    resp = service.delete(id)
    if not resp:
        msg = "No se pudo eliminar el Producto"
    return jsonify(msg), 204