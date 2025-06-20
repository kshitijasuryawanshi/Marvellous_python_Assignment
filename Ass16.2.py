

def main():
    fobj=open("data.txt","r")
    
    data=fobj.read()
    print("Content in file is:",data)


if __name__=="__main__":
    main()