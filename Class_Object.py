"""
Object is a instace of class
"""

class car(object):
    def __init__(self, make,year):
        self.makeof_Car=make,
        self.year=year

# c1=car("bmw")
# print(c1.makeof_Car)
# c1=car("hyundai")
# print(c1.makeof_Car)
c2=car('Maruti', 2019)
print(c2.makeof_Car)
print(c2.year)

c3=car("Innova", 2020)
print(c3.makeof_Car)
print((c3.year))
