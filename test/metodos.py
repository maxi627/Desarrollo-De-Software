from abc import ABC, abstractmethod
from flask import current_app
from app import create_app, db
import unittest

"""
    Test User model
    Aplicando principios como DRY (Don't Repeat Yourself) y KISS (Keep It Simple, Stupid).
  """
class Test_setUp(unittest.TestCase, ABC):
    @abstractmethod
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
class Test_teardown(unittest.TestCase,ABC):
    @abstractmethod
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
class Test_app(unittest.TestCase,ABC):
    def test_app(self):
        self.assertIsNotNone(current_app)