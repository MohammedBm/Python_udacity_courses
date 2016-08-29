
import os

def rename_files ():
    
    #1 got file inside
    file_list = os.listdir("/Users/Coding/Downloads/prank/")
    #print(file_list)
    os.chdir("/Users/Coding/Downloads/prank")
    saved_path = os.getcwd()
    print("current working direvtory is"+saved_path)

    #2 rename filename

    for file_name in file_list:
        os.rename(file_name, file_name.translate ( "0123456789"))

    os.chdir(saved_path)

rename_files ()
