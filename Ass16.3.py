
import os

def main():
    print("Enter name of the file which you want to open")
    filename=input()

    ret=os.path.exists(filename)

    if(ret!=True):
        print("File is not Present")
    else:
        fobj=open(filename,"r")
        content = fobj.read()
        word=content.split()
        
        with open(filename, 'r') as fp:
            for count, line in enumerate(fp):
                pass
            print('Total Lines', count + 1) 

        countw=0
        for line in fobj:
            if word in line:
                countw=countw+1
        print(count)


if __name__=="__main__":
    main()

