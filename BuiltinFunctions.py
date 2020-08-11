"""
max() its takes mnumber of arguments and retuns the largest one.
min() its takes number of arguments and returns smallet one.
typs() its returns the type of the data it receives as an argument

abs() its returns the absulate value of the number's distance from 0.
its always returns the type of the data  and it's only takes single number
"""

def lartest_num(*args):
    print(max(args))

lartest_num(10,20,2,4,56,3)


def smallest_num(*args):
    print(min(args))

smallest_num(1,0.4,4,0)


def find_abs(a):
    print(abs(a))

find_abs(4)
find_abs(-6)

print(type(1))
print(type("abc"))
print(type(1.3))
