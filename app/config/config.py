"""
Configuración de la aplicación
"""
# Importación de módulos necesarios
from pathlib import Path  # Para manejar rutas de archivos y directorios
import os  # Para interactuar con el sistema operativo
from dotenv import load_dotenv  # Para cargar variables de entorno desde un archivo .env

# Obtiene la ruta absoluta del directorio base de la aplicación
basedir = os.path.abspath(Path(__file__).parents[2])

# Carga las variables de entorno desde el archivo .env en el directorio base
load_dotenv(os.path.join(basedir, '.env'))

# Clase base de configuración de la aplicación
class Config(object):
    TESTING = False  # Configuración de prueba desactivada por defecto
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones en SQLAlchemy
    SQLALCHEMY_RECORD_QUERIES = True  # Habilita el registro de consultas en SQLAlchemy
    
    @staticmethod
    def init_app(app):
        pass  # Método para inicializar la aplicación (puede implementarse en subclases)
        
# Configuración específica para el entorno de desarrollo
class DevelopmentConfig(Config):
    TESTING = True  # Activa el modo de prueba
    DEBUG = True  # Activa el modo de depuración
    FLASK_ENV = 'development'  # Define el entorno como desarrollo
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # Habilita el seguimiento de modificaciones en SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost/app_flask'
"""
Configuración en entorno de producción
"""
# Configuración específica para el entorno de producción
class ProductionConfig(Config):
    FLASK_ENV = 'production'  # Define el entorno como producción
    DEBUG = False  # Desactiva el modo de depuración
    TESTING = False  # Desactiva el modo de prueba
    SQLALCHEMY_RECORD_QUERIES = False  # Desactiva el registro de consultas en SQLAlchemy
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:12345@localhost/app_flask'
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)  # Llama al método init_app de la clase base Config para inicializar la aplicación

"""
Factory para la configuración de la aplicación
param: entorno -> Entorno de ejecución de la aplicación
"""
# Factory para seleccionar la configuración de la aplicación según el entorno
def factory(entorno: str):
    # Diccionario que mapea nombres de entornos con sus respectivas configuraciones
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[entorno];   # Retorna la configuración correspondiente al entorno dado

