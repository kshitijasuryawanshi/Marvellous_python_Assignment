
import os

def main():
    print("Enter name of the file which you want to open")
    filename=input()

    ret=os.path.exists(filename)

    if(ret!=True):
        print("File is not Present")
    else:
        fobj=open(filename,"r")
        d=input()
        count=0

        for line in fobj:
            if d in line:
                count=count+1
        print(count)


if __name__=="__main__":
    main()

