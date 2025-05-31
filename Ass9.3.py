import multiprocessing.process
import time
import os 
import multiprocessing

def Fact(no):
    factorial=1
    for j in range(1,no+1):
        factorial=factorial*j
    return factorial

        

def main():
    n=int(input("Enter size of list:"))
    data=[]
    for i in range(n):
        no=int(input())
        data.append(no)

    print(data)

    #p=multiprocessing.Process(target=Fact,args=(data,))
    ##p.join()
    p=multiprocessing.Pool(n)
    ret=p.map(Fact,data)
    print(ret)

if __name__=="__main__":
    main()