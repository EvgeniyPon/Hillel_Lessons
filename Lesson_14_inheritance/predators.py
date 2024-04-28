from Classes import *

class Predators(LandMammal):
    def __init__(self, name, type_, area, legs, food):
        super().__init__(name, type_, area, legs)
        self.food = food

    def feed(self):
        return f'{self.type_} {self.name} is eat a steak from a {self.food}'


