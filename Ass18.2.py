import os

def main():
    print("Enter name of the file which you want to open")
    filename=input()

    ret=os.path.exists(filename)

    if(ret!=True):
        print("File is not Present")
    else:
        print("File is present in the current directory")
        fobj=open(filename,"r")

        data=fobj.read()

        print("Data from file is:",data)



if __name__=="__main__":
    main()