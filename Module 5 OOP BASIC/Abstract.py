from abc import ABC, abstractmethod
# abstract base class

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('hey nana!, eating banana')
    
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        self.category = 'Monkey'
        super().__init__()
    
    # overriding
    # def eat(self):
    #     print('hi na na na, i am eating banana')

layka = Monkey('lucky')
layka.eat()