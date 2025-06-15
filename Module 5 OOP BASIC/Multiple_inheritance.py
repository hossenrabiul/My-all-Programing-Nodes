class Family:
    def __init__(self, address) -> None:
        self.address = address

    def __repr__(self) -> str:
       return f' {self.address}'

class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level
    
    def __repr__(self) -> str:
        return f'{self.id}, {self.level}'

class sports:
    def  __init__(self, game) -> None:
        self.game = game

class Student(Family, School, sports):
    def __init__(self, address, id, level, game) -> None:
        School().__init__(self, id, level)
        # sports().__init__(self, game)
        Family().__init__(address)

    # def __repr__(self) -> str:
    #     return super().__repr__()
    
my_family = Student('khatunganj', 2, 3, 'football')
print(my_family)

# your_family = Family('khatunganj')
# your_family = School(2, 56)
# print(your_family)