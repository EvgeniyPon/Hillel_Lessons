from abc import abstractmethod
class Mammal:
    def __init__(self, name, type_, area):
        self.name = name
        self.type_ = type_
        self.area = area

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def dance(self):
        pass
