
def main():

    fobj2=open("number.txt","w")

    for i in range(10):
        data=int(input())
        fobj2.write(str(data)+"\n")
    
    fobj2.close()
        
    


if __name__=="__main__":
    main()