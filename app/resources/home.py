from flask import jsonify, Blueprint  # Importa las funciones jsonify y Blueprint desde Flask

home = Blueprint('home', __name__)  # Crea un blueprint llamado 'home'

@home.route('/', methods=['GET'])
def index():
    resp = jsonify("OK")  # Crea una respuesta JSON con el mensaje "OK"
    resp.status_code = 200  # Establece el código de estado HTTP 200 (OK)
    return resp  # Devuelve la respuesta JSON con el mensaje "OK" y el código de estado 200
