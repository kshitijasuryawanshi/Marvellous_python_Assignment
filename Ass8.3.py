import threading

def Evenlist(no):
    sum=0
    for i in no:
        if (i%2==0):
            sum=sum+i
    print("Sum of even number:",sum)

def Oddlist(no):
    sum=0
    for i in no:
        if (i%2!=0):
            sum=sum+i
    print("Sum of Odd number:",sum)

def main():
    n=int(input("Enter the size of list:"))
    data=[]
    for i in range(0,n):
        no=int(input())
        data.append(no)

    

    print(data)
    T1=threading.Thread(target=Evenlist,args=(data,))
    T2=threading.Thread(target=Oddlist,args=(data,))
    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("End of main")

if __name__=="__main__":
    main()
    
