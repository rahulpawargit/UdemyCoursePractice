#method overriding

class parent(object):
    def __init__(self):
        print("This is contructor")

    def first(self):
        print("This is first method in Parent class")

    def second(self):
        print("This is second method of second in parent class")


class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("This is constucor method in Child class")
    def third(self):
        print("This is thired method in child class")
    def first(self):
        super(child,self).first()
        print('This is overried method in child class')


obj1=child()
obj1.first()
obj1.second()
obj1.third()

