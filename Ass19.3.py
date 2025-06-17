import os 
import sys
import shutil


def CopyingFiles(SourceDir,DestDir):

    SourceDir=os.path.abspath(SourceDir)
    DestDir=os.path.abspath(DestDir)

    if not os.path.exists(DestDir):
        os.makedirs(DestDir)
    else:
        print("Folder Already Exist")

    for i in os.listdir(SourceDir):
        sourcepath=os.path.join(SourceDir,i)
        destpath=os.path.join(DestDir,i)

        if os.path.isfile(sourcepath):
            shutil.copy2(sourcepath,destpath)


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

    elif(len(sys.argv) == 3):
        CopyingFiles(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(Border)

if __name__=="__main__":
    main()