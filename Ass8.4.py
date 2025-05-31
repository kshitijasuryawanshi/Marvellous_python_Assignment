import threading
import os

def Small(str):
    print("PID is :",os.getpid())
    print("name of thread:",threading.current_thread().name)
    for i in str:
        if(i.islower()):
            print(i,end=" ")
    print("\n")

def Digit(str):
    print("PID is :",os.getpid())
    print("name of thread:",threading.current_thread().name)
    for i in str:
        if(i.isdigit()):
            print(i,end=" ")
    print("\n")

def  Capital(str):
    print("PID is :",os.getpid())
    print("name of thread:",threading.current_thread().name)
    for i in str:
        if(i.isupper()):
            print(i,end=" ")
    print("\n")

        

def main():
    str=input()

    T1=threading.Thread(target=Digit,args=(str,))
    
    T2=threading.Thread(target=Capital,args=(str,))

    T3=threading.Thread(target=Small,args=(str,))
    print("Digits in string are:")
    T1.start()
    T1.join()
    print("End of 1st Thread !")
    print("Capital letters in string are:")
    T2.start()
    T2.join()
    print("End of 2nd Thread !")
    print("Small letters in string are:")
    T3.start()
    T3.join()
    print("End of 3rd Thread !")

    print("End of main")

if __name__=="__main__":
    main()
    
