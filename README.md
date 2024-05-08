#DEPENDENCIAS
# TODO LIST!

Ejemplo en Flask y MySQL 

# Requerimientos previos
Para la librería **mysqlclient** se necesita previamente tener instalado lo siguiente:
**Linux**:
sudo apt-get install python3-dev default-libmysqlclient-dev libmysqlclient-dev build-essential
$ export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
$ export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
Referencia: https://pypi.org/project/mysqlclient/
Como alterntativa se tiene **mysql-connector-python** una libraria totalmente escrita en python y que no depende de la librerias en C de MySQL
Referencias: 
https://dev.mysql.com/doc/connector-python/en/
https://pypi.org/project/mysql-connector-python/ 
# Pasos:
Ejecutar:
flask db init
flask db migrate -m "Migración inicial"
Referencia: https://flask-migrate.readthedocs.io/en/latest/#installation