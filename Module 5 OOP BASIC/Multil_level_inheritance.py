class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def move(self):
        return f'ik'
    
    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'
    
class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class Track(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)

class PickUpTruck(Track):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'{self.seat}, {self.name}, {self.temperature}')
        return super().__repr__()

Green_line = ACBus('green', 500000, 22, 16)
print(Green_line)