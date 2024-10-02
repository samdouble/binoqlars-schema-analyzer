from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def __init__(self):
        pass
