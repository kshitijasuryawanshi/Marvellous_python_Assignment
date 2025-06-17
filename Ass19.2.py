import os 
import sys


def ChangingFileExtension(Directory,Extension,NewExtension):


    flag = os.path.isabs(Directory)

    if(flag == False):
        DirectoryName = os.path.abspath(Directory)
    else:
        DirectoryName=Directory

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(Directory)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            if fname.endswith(Extension):
                oldpath=os.path.join(FolderName,fname)
                base,_=os.path.splitext(fname)
                newfilename=base+NewExtension
                newpath=os.path.join(FolderName,fname)
                os.rename(oldpath,newpath)
                



def main():

    Border=51*'-'
    print(Border)
    print("--------------- Assignment Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory Expected_Extention")
            print("Please provide valid absolute path")

    elif(len(sys.argv) == 4):
        ChangingFileExtension(sys.argv[1], sys.argv[2],sys.argv[3])

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print(Border)

if __name__=="__main__":
    main()