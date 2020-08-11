"""
for loop used to execute the statements repeatdly
Conditions are used to stop execution of loops
Iterable items are String, List, Dictionary Tuples

"""
#
# str="abcabc"
#
# for i in str:
#     # print (i, end=' ')
#     if i=="a":
#         print("A", end='')
#     else:
#         print(i, end='')
#
# print()
# cars=['bmw', 'scoda','desire']
# print(cars)
# for j in cars:
#     print(j, end='')
#
# print()
#
# print("#" * 10)
#
# nums=[1,2,3,4,5]
# for a in nums:
#     print (a * 10)
#
# print()

# dict={'a':1, 'b':2, 'c':3, 'd':5}
# for i in dict:
#      print(i+ " " +str(dict[i]))

# mu_string ='abcabc'
#
# for i in mu_string:
#      if i=='a':
#           print('A', end=' ')
#
#      else:
#       print(i, end= ' ')


## Zip Function for iterating the multiple list

l1=[1,2,3,40,50,90,100]
l2=[6,7,8,9,10]
l3=[11,12,13,14,34,23,54]

for l1, l2, l3 in zip(l1,l2,l3):
     print(l1,l2,l3)

