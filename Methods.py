"""
Methods are bolck of the statements which are used to perform specific task
"""

def sum(a,b):
    return (a+b)


addition=sum(4,5)
print(addition)

def ismetro(city):
    l=['pune', 'mumbai', 'nagpur']

    if city in l:
         return True
    else:
        return False


available= ismetro('fh ')
print(available)