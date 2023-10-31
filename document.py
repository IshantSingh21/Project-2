import os
import shutil

fromdir="c:/Users/MICROSOFT/Downloads"
todir= "c:/Users/MICROSOFT/Documents"
listofFiles= os.listdir(fromdir)
print(listofFiles)

for file in listofFiles:
    name,extension= os.path.splitext(file)
    print(extension)