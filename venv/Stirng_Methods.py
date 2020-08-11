"""
String Methods
"""

str1= "ABC"[1]
print(str1)

str2= "PQRS"
str3=str2[3]
print(str3)

"""
len()
upper()
lower()
str()
"""

str4= "This is my string 3"
print(str4.upper())
print(str4.lower())
print(len(str4))

str5="Connect me"


"""
Concatnation
"""

print(str5 +"--> ", str4)

"""
Replace
"""

s1= "1abc2abc3abc4abc"
print(s1.replace('abc','ABC'))
print(s1.replace('abc','ABC',2))


"""
Sub String
"""
s2=s1[0:4]
print(s2)

"""
Step sub string
"""

s3=s1[0:8:2]
print(s3)

