import threading
import time
import multiprocessing

def Displaysum(no):
    sum=0
    for i in range(1,no):
        sum=sum+1
    return sum


def main():
    start_time=time.time()
    T1=threading.Thread(target=Displaysum,args={100000000})
    T1.start()
    T1.join()
    end_time=time.time()
    print("Required time for execution of program with Thread",end_time-start_time)

    start_time=time.time()
    T2=multiprocessing.Process(target=Displaysum,args={100000000})

    T2.start()
    T2.join()
    end_time=time.time()
    print("Required time for execution of program with multiprocessing:",end_time-start_time)
    

    start_time=time.time()
    Displaysum(100000000)
    end_time=time.time()
    print("Required time for execution of program without Threading",end_time-start_time)
    print("End of main")

if __name__=="__main__":
    main()
    
