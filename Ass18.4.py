
def main():

    print("Enter name of the file which you want two compare and check contains same content:")
    filename1=input()
    filename2=input()

    fobj1=open(filename1,"r")
    fobj2=open(filename2,"r")
    data1=fobj1.read()
    data2=fobj2.read()

    if(data1==data2):
        print("Success..!")
    else:
        print("Failure..!")



if __name__=="__main__":
    main()