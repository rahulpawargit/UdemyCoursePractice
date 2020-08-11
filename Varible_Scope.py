"""
Varibale scope
"""


#
# a=10
#
# def variable_scope(a):
#     print("Value of inside a" +str(a))
#     a=5
#     print("Value of updated a" +str(a))
#
# print("Value of ourside a=" +str(a))
# variable_scope(3)

# using Global keyword


a=10

def variable_scope():
    global a
    print("Value of inside a" +str(a))
    a=5
    print("Value of updated a" +str(a))

print("Value of ourside a=" +str(a))
variable_scope()




