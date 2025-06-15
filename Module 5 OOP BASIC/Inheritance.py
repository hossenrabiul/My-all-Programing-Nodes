# base class, parent class, common attrubute + functionality class
# derived class, child class, uncommon attribute + functionality class

class Gedget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'running laptop: {self.brand}'
        

class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    # def run(self):
    #     return f'running laptop: {self.brand}'
    
    def coding(self):
        return f'lerning python and practicing'
    
class Phone(Gedget):
    def __init__(self, brand, price, color, origin, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    # def run(self):
    #     return f'i am running {self.dual_sim} phone'

    def __repr__(self) -> str:
        return f'phone: {self.dual_sim}, price: {self.price}, Brand: {self.brand}, origin: {self.origin}'

class Camera:
    def __init__(self, pixel):
        self.pixel = pixel 

my_phone = Phone('iphone', 120000, 'black', 'china', True)
print(my_phone)
print(my_phone.brand)