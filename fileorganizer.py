import os 
import subprocess
import shutil

#this script was written mostly by a tutorial and contains many things I need to understand better
def organize():
    fileExtensions = {
        "Pictures": ["png", "img", "jpeg", "jpg"],
        "Videos": ["mp4", "mkv", "mov"],
        "Scripts": ["py", "js", "cpp"],
        "Documents": ["txt", "pdf", "md", "html"],
        "Compressed Files": ["deb", "gz", "xz", "zip", "7z"]
    }

    location = input("What location do you want to organize? ")
    for name in os.listdir(location):
        path = os.path.join(location, name)

        if os.path.isfile(path):
            fileExtension = os.path.splitext(name)[1].lower()
            targetFolder = "other"

            for folder, extensions in fileExtensions.items():
                if fileExtensions in extensions:
                    targetFolder = folder
                    break
            
            
            target_path = os.path.join(location, targetFolder, name)
            os.makedirs(os.path.join(location, targetFolder), exist_ok=True)
            shutil.move(path, target_path)
organize()

   
   

            
