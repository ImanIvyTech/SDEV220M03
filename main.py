# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


things = ['mozzarella', 'cinderella', 'salmonella']
things[1] = 'Cinderella'
print(things)
things[0] = 'MOZZARELLA'
print(things)
things.pop(3)
print(things)


def good():
    goood = ['Harry', 'Ron', 'Hermione']
    print(goood)


def get_odds():
    x = 0
    while x > 3:
        for number in range(10):
            if number % 2 != 0:
                print(number)
                x += 1
    print(number)


class Vehicle:
    attr1 = 'car'


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display(self):
        print(self.year, self.make, self.model, self.doors, self.roof)
