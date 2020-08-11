"""
Positional parameters are optional parameter
And can be assigned the default values, if no values provided outsite

"""

def parameter(a=10, b=23):
    return (a+b)

add=parameter(b=8)
print(add)