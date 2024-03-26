from abc import ABC, abstractmethod


class Super(ABC):

    @staticmethod
    @abstractmethod
    def find(substring: str, text: str):
        pass

    @classmethod
    def name(cls) -> str:
        return cls.__name__

    @classmethod
    def findall(cls, substring: str, text: str) -> list:
        return list(cls.find(substring, text))
