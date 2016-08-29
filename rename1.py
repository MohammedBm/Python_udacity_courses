import os

def rename_files():
#(1) get file name from a folder
    file_list = os.listdir("/Users/Coding/Downloads/prank-2")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working Directory is "+saved_path)
    os.chdir("/Users/Coding/Downloads/prank-2")
#(2) for each file,rename filename
    for file_name in file_list:
        print("Old_Name - "+file_name)
#strip() returns a copy of the string in which all chars have been stripped from the beginning of the string (default whitespace characters)eg.str.lstrip([chars])
        print("New_Name -"+file_name.lstrip("01234567890"))
        os.rename(file_name,file_name.lstrip("01234567890"))
    os.chdir(saved_path)

rename_files()
