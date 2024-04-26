from main_class import *
class LandMammal(Mammal):
    def __init__(self, name, type_, area, legs):
        super().__init__(name, type_, area)
        self.legs = legs

    def move(self):
        return f'{self.type_} {self.name} is running by my {self.legs} legs'

    def dance(self):
        return f'{self.type_} {self.name} is dancing with my {self.legs} legs'

class MarineMammal(Mammal):
    def __init__(self, name, type_, area, flippers):
        super().__init__(name, type_, area)
        self.flippers = flippers

    def move(self):
        return f'{self.type_} {self.name} is swimming by his {self.flippers} legs'

    def dance(self):
        return f"{self.type_} {self.name} can't dance with his {self.flippers} flippers"


if __name__ == '__main__':
    a = MarineMammal('John', 'Dolphin', 'ocean', 3)
    b = LandMammal('Nastya', 'Human', 'Kyiv', 2)
    print(f' {a.move()} \nand\n {b.dance()}')