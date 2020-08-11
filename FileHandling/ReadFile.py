"""
File i/o
Reading a file-  read()
Reading file line by line - readline()
"""

my_file=open("FistFile.txt", "r")
print(my_file.read())


# //Read file line by line

my_file_readline=open("FistFile.txt", "r")

for items in my_file_readline:

     print((items))

my_file_readline.close()
