class Car:

    def __init__(self, make, model, year, colors):
        self.make = make
        self.model = model
        self.year = year
        self.colors = colors
    def drive(self):
        print('This ' + self.model + '  is driving!')

    def stop(self):
        print('This ' + self.model + ' is stopped!')