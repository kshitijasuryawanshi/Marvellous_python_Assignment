import os

def main():
    print("Enter name of the file which you want to open")
    filename=input()

    ret=os.path.exists(filename)

    if(ret!=True):
        print("File is not Present")
    else:
        fobj=open(filename,"r")

        data=fobj.read()
        

        fobj1=open("Demo2.txt","x")
        fobj1.write(data)








if __name__=="__main__":
    main()