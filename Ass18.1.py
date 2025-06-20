import os 



def main():
    print("Enter file name which you want to check")
    filename=input()


    result=os.path.exists(filename)

    if(result==True):
        print("File is present in current directory")
    else:
        print("File is not present in current directory")



if __name__=="__main__":
    main()