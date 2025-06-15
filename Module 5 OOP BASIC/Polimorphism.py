class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('animal make some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meow , meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('gheo gheo')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('beh beh beh')
    

don = Cat('Don')
don.make_sound()
shepart = Dog('local shepard')
shepart.make_sound()

mess = Goat('L M')
mess.make_sound()

less = Goat('gora gori')

Animals = [less, mess, don, shepart]

for animal in Animals:
    animal.make_sound()