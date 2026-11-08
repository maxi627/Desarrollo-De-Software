# Desarrollo de Software: API de e-commerce

API REST de un e-commerce hecha con **Flask** para la materia Desarrollo de Software (3º año de Ingeniería en Sistemas). Gestiona usuarios, productos, categorías y detalles de orden. La arquitectura está en capas y aplica principios de diseño como **SOLID**, **DRY** y **KISS**, además de los patrones **Repository** y **Factory**.

- **Stack:** Python 3.11 · Flask 3 · Flask-SQLAlchemy · Flask-Migrate · Marshmallow · MySQL (PyMySQL) · Werkzeug / Passlib · unittest
- **URL base:** `http://localhost:5000/api/v1`

> Este proyecto es la versión monolítica del e-commerce. La continuación con microservicios está en [ms_producto](https://github.com/maxi627/ms_producto), [ms_stock](https://github.com/maxi627/ms_stock), [ms_pagos](https://github.com/maxi627/ms_pagos), [ms_compra](https://github.com/maxi627/ms_compra) y [base_ms](https://github.com/maxi627/base_ms).

---

## Modelo de datos

![Diagrama entidad-relación del e-commerce](diagrama_ecommerce.png)

| Entidad | Tabla | Campos | Relaciones |
|---|---|---|---|
| `User` | `users` | `id`, `nombre`, `email` (único), `password` (se guarda hasheada), `id_detalle` | Tiene órdenes (`Detalle_Orden`) |
| `Producto` | `Producto` | `id_producto`, `nombre`, `precio`, `stock`, `id_categoria` | Pertenece a una `Categoria` y aparece en órdenes |
| `Categoria` | `Categorias` | `id_categoria`, `nombre` | Agrupa productos |
| `Orden` | `Detalle_Orden` | `id_detalle`, `id_producto`, `cantidad`, `precio` | Referencia un `Producto` y un `User` |

El diagrama de clases en PlantUML está en [`app/diagrama.puml`](app/diagrama.puml) y el editable de draw.io en [`diagrama_ecommerce.drawio`](diagrama_ecommerce.drawio).

## API

Todas las rutas llevan el prefijo `/api/v1`.

| Recurso | Método | Ruta | Descripción |
|---|---|---|---|
| Home | GET | `/` | Health check, responde `"OK"` |
| Usuarios | GET | `/Users` | Lista los usuarios |
| | GET | `/Users/<id>` | Obtiene un usuario |
| | GET | `/Users_inicial/<inicial>` | Filtra los usuarios por la inicial del nombre |
| | POST | `/Users` | Crea un usuario |
| | PUT | `/Users/<id>` | Actualiza un usuario (la contraseña se vuelve a hashear) |
| | DELETE | `/Users/<id>` | Elimina un usuario |
| Productos | GET | `/productos` | Lista los productos |
| | GET | `/productos/<id>` | Obtiene un producto (incluye su categoría) |
| | POST | `/productos` | Crea un producto |
| | PUT | `/productos/<id>` | Actualiza un producto |
| | DELETE | `/productos/<id>` | Elimina un producto |
| Categorías | GET | `/categorias` | Lista las categorías (con sus productos) |
| | GET | `/categorias/<id>` | Obtiene una categoría |
| | POST | `/categorias` | Crea una categoría |
| | PUT | `/categorias/<id>` | Actualiza una categoría |
| | DELETE | `/categorias/<id>` | Elimina una categoría |
| Órdenes | GET | `/orden` | Lista los detalles de orden |
| | GET | `/orden/<id>` | Obtiene un detalle de orden (incluye el producto) |
| | POST | `/orden` | Crea un detalle de orden |
| | PUT | `/orden/<id>` | Actualiza un detalle de orden |
| | DELETE | `/orden/<id>` | Elimina un detalle de orden |

Códigos de respuesta: `200` OK · `201` creado · `204` eliminado.

Ejemplos:

```bash
# Crear una categoría
curl -X POST http://localhost:5000/api/v1/categorias \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Periféricos"}'

# Crear un producto en esa categoría
curl -X POST http://localhost:5000/api/v1/productos \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Teclado mecánico", "precio": 45000, "stock": 10, "id_categoria": 1}'
```

## Arquitectura

```
app/
├── __init__.py      # Application factory: create_app() registra extensiones y blueprints
├── config/          # Configuración por entorno (development / production) con patrón Factory
├── models/          # Modelos SQLAlchemy: User, Producto, Categoria, Orden
├── mapping/         # Schemas Marshmallow para validar y serializar (incluye relaciones anidadas)
├── repositories/    # Acceso a datos (patrón Repository)
├── services/        # Lógica de negocio y seguridad de contraseñas
└── resources/       # Blueprints Flask con los endpoints REST
app.py               # Punto de entrada: crea las tablas y levanta el servidor
test/                # Tests con unittest
```

El flujo de una petición es `resource` → `service` → `repository` → `model`. En el camino, los schemas de `mapping` validan la entrada y serializan la salida.

### Principios de diseño aplicados

| Principio / patrón | Dónde |
|---|---|
| **Single Responsibility** | Cada capa tiene una sola responsabilidad. `SecurityManager` solo se ocupa del hash y la verificación de contraseñas |
| **Interface Segregation** | Las interfaces de repositorio están separadas por operación (`Repository_save`, `Repository_get`, `Repository_create`, `Repository_update`, `Repository_delete`) como clases abstractas (`ABC`). Cada repositorio implementa solo las que necesita |
| **Liskov Substitution / Dependency Inversion** | `SecurityManager` depende de la abstracción `AbstractSecurity`. `WerkzeugSecurity` y `PassLibSecurity` se pueden intercambiar sin cambiar el resto del código |
| **Factory** | `create_app()` (application factory) y `config.factory(entorno)` para elegir la configuración |
| **Repository** | `app/repositories/` aísla el acceso a la base de datos de la lógica de negocio |
| **DRY / KISS** | `test/metodos.py` reúne el `setUp` / `tearDown` comunes de los tests |

## Instalación

### Requisitos previos

- Python 3.11
- Un servidor MySQL con una base llamada `app_flask`

La librería **mysqlclient** (incluida en `requirements.txt`) necesita las librerías de desarrollo de MySQL:

```bash
# Linux
sudo apt-get install python3-dev default-libmysqlclient-dev libmysqlclient-dev build-essential
export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
```

Referencia: <https://pypi.org/project/mysqlclient/>. La conexión de la app usa **PyMySQL**, que está escrita en Python puro. Otra alternativa sin dependencias de C es [mysql-connector-python](https://pypi.org/project/mysql-connector-python/).

### Pasos

```bash
# 1. Entorno virtual y dependencias
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Base de datos
mysql -u root -p -e "CREATE DATABASE app_flask"
```

La cadena de conexión se define en [`app/config/config.py`](app/config/config.py). Por defecto es `mysql+pymysql://root:12345@localhost/app_flask`; ajustala a tu usuario y contraseña de MySQL.

El entorno se elige con la variable `FLASK_ENV` (`development` por defecto, o `production`), que también se puede definir en un archivo `.env` en la raíz.

## Ejecución

```bash
python app.py          # o ./boot.sh
```

`app.py` crea las tablas si no existen (`db.create_all()`) y levanta el servidor en <http://localhost:5000/api/v1>.

### Migraciones (opcional)

En lugar de `db.create_all()`, el esquema se puede manejar con [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/#installation):

```bash
flask db init
flask db migrate -m "Migración inicial"
flask db upgrade
```

## Tests

```bash
python -m unittest discover -s test -p "test*.py" -v
```

| Archivo | Qué prueba |
|---|---|
| `test/test_app.py` | Que la app se crea correctamente |
| `test/test_db.py` | Conexión a la base de datos |
| `test/test_categoria.py` | Modelo `Categoria` |
| `test/test_producto.py` | Guardar, buscar, listar y eliminar productos |
| `test/test_orden.py` | Guardar, buscar, listar y eliminar órdenes |
| `test/test_usuario.py` | CRUD de usuarios, que la contraseña se guarde hasheada, `check_auth`, intercambio de Werkzeug por Passlib y el endpoint `POST /Users` |

> ⚠️ No hay una configuración separada para tests: corren contra la base de desarrollo, y varios terminan con `db.drop_all()`, que **borra las tablas**. Usá una base descartable para correrlos.

## Licencia

[Apache 2.0](LICENSE)
