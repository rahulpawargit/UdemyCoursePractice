import math
from Inheritance import Car
def builtinmodule():
    a=math.sqrt(100)
    print(a)
    b=math.radians(50)
    print(b)
    print(math.remainder(10,3))

def carDescription(self):

    Car.drive()
    Car.stop(self)

builtinmodule()

Car.stop()