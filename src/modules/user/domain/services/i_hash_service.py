from abc import ABC, abstractmethod

class IHashService(ABC):
    @abstractmethod
    def hash(self, value:str) -> str: ...

    @abstractmethod
    def compare(self, value:str, hashed_value:str) -> bool: ...