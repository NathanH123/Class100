class Car():
    def __init__(self, brand, color, mph, gear):
        self.brand=brand
        self.color=color
        self.mph=mph
        self.gear=gear
    def start(self):
        print('The car has started')
    def stop(self):
        print('The car has stopped')
bmw=Car('BMW','blue', 250, 6)
print(bmw.brand)
print(bmw.start())
print(bmw.stop())
print(bmw.color)
print(bmw.mph)
print(bmw.gear)