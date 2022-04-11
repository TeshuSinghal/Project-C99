import os
import time
import os
import shutil

path= input("Enter the name of the folder")
days= 30
seconds = time.time()-(days*24*60*60)

if os.path.exists(path):
    for root_folder, folders, files in os.walk(path):
        if(seconds >= getFileFolderAge(rootFolder)):
            remove_folder(root_folder)
                #Create a function for removing the folder
                
def remove_folder(path):
    os.remove(path)





def getFileFolderAge(path):
    ctime= os.stat(path).st_ctime
    return ctime