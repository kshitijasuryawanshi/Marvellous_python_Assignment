import threading

def EvenFact(No):
    for i in range(1,No+1):
        if(No%i==0):
            if(i%2==0):
                print(i)
    

def OddFact(No):
    for i in range(1,No+1):
        if(No%i==0):
            if(i%2!=0):
                print(i)



def main():
    n=int(input("Enter Number:"))
    T1=threading.Thread(target=EvenFact,args={n})
    T2=threading.Thread(target=OddFact,args={n})
    print("EvenFactors are:")
    T1.start()
    T1.join()
    print("OddFactors are:")
    T2.start()
    T2.join()
    
    print("End of main")

if __name__=="__main__":
    main()