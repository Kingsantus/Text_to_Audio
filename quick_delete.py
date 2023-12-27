import os

file_path = r'/Users/west/Documents/learn/automate/git.xlsx'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted!")
else:
    print("This file does Not Exist!!!")