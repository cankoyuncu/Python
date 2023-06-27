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
#result = os.stat("date.py")
#result = datetime.datetime.fromtimestamp(result.st_mtime) #change time format
#result = result.st_size/1024 

#os.system("notepad.exe") #open notepad

#os.rmdir("newfile") #remove file if dont have subdirectory
#os.removedirs("newfolder/newfolder2") #remove file if have subdirectory

#path
#result = os.path.abspath("date.py") #full path
#result = os.path.dirname(os.path.abspath("date.py"))
#result = os.path.isdir("C:\\Users\\user\\Desktop\\Python\\15_Web_Scraping\\os.py")
#result = os.path.isfile("C:\\Users\\user\\Desktop\\Python\\15_Web_Scraping\\os.py")
#result = os.path.join("C:\\","deneme","deneme1") #merge path
#result = os.path.split("C:\\deneme")
#result = os.path.splitext("os.py")

print(result)