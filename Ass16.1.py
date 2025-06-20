

def main():
        fobj1=open("student.txt","w")
         
        for i in range(5):
            data=input()
            fobj1.write(data+"\n")
        fobj1.close


if __name__=="__main__":
    main()