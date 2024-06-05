from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Type
from sqlalchemy.orm import Session
from app import db


T = TypeVar('T')


class Test_Setup(ABC):
    @abstractmethod
    def Setup(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
    pass  
class Test_create(ABC):
    
    @abstractmethod
    pass
    
class Test_update(ABC):
    
    @abstractmethod
    def update(self, id, entity: T) -> T:
        pass
    
class Test_delete(ABC):
    
    @abstractmethod 
    def delete(self, id) -> bool:
        pass