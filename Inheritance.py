# Inheritance which access the proprities of another class

class Car(object):
    def __init__(self):
        print("This is self method of Car class....")
    def drive(self):
        print("This is the Driver method")

    def stop(self):
        print("This is stop method")

class Xcent(Car):
    def __init__(self):
        Car.__init__(self)
        print("This is self method of Xcnet class")
    def wheels(self):
        print("This vehicla has 4 wheels")

a=Car()
a.drive()
a.stop()

b=Xcent()
b.drive()
b.stop()
b.wheels()
