class Laptop:
    def __init__(self, brand, price, colour, memory) -> None:
        self.brand = brand
        self.price = price
        self.colour = colour
        self.memory = memory

    def run(self):
        return f'running laptop: {self.brand}'
    
    def coding(self):
        return f'lerning python and practicing'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim):
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim