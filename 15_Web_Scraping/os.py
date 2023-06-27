import os
import datetime

result = dir(os)
result = os.name

#os.chdir('..//..') #change directory
#os.chdir('C:\\')

#os.mkdir("newdirector") #create directory
#os.makedirs("newfolder/newfolder2") #create directory and subdirectory


#result = os.listdir() #list file
#result = os.listdir('C:\\') #list file in C:\\

# for file in os.listdir():
#     if file.endswith('.py'):
#         print(file)

#result = os.getcwd() #active location 

#result = os.stat("date.py") #file information

result = os.stat("_datetime.py")
result = result.st_size/1024 

print(result)