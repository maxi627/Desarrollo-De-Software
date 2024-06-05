import unittest
from sqlalchemy import text
import sys
sys.path.append('d:/Usuarios/Documents/3ro Ing. En Sistemas/Desarrollo De Software')
from app import create_app, db


class ConnectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            with db.engine.connect() as connection:
                 db.drop_all()
        self.app_context.pop()

    def test_db_connection(self):
        result = db.session.query(text("'Hello world'")).one()
        self.assertEqual(result[0], 'Hello world')
    
if __name__ == '__main__':
    unittest.main()
