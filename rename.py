import os
def rename_file():
    f=os.listdir(r"d:\prank")
    os.chdir(r"d:\prank")
    print("newfile  in "+os.getcwd())
    for file_name in f:
        print("OLD NAME -"+file_name)
        print("NEW NAME -"+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print (file_name)
rename_file()
    
