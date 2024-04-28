from Classes import *
from predators import *


if __name__ == '__main__':
    a = MarineMammal('John', 'Dolphin', 'ocean', 3)
    b = LandMammal('Nastya', 'Human', 'Kyiv', 2)
    c = Predators('Vasya', 'Lion', 'Africa', 4, 'Cow')
    print(f' {a.move()} \nand\n {b.dance()}\nand\n {c.feed()}')