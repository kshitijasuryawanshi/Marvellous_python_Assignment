import threading

def DisplayT_1(no):
    for i in range(1,no+1):
        print(i,end=" ")
    print("\n")

def DisplayT_2(no):
    for i in range(no,0,-1):
        print(i,end=" ")
    print("\n")

def main():
    n=int(input("Enter the size of list:"))
    T1=threading.Thread(target=DisplayT_1,args={n})
    T2=threading.Thread(target=DisplayT_2,args={n})
    T1.start()
    

    T1.join()
    print("End of 1st Thread !")
    T2.start()
    T2.join()
    print("End of 2nd Thread !")
    print("End of main")

if __name__=="__main__":
    main()
    
