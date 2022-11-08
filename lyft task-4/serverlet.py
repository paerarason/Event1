from abc import ABC, abstractmethod


class serverlet(ABC):
    @abstractmethod
    def needs_service(self):
        pass