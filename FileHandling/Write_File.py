"""
File i/o
w- Write a file
r- Read only mode
r+- Read and write mode
a- Append mode

"""

def file_writing():
  my_list=[1,2,3,4]
  my_File=open("FistFile.txt", 'w')
  my_Dict={'Type':'Car', 'Model':'Nexa','Year':'2020'}

  for items in my_list,my_Dict:
        my_File.write(str(items)+'\n')
  my_File.close()



file_writing()