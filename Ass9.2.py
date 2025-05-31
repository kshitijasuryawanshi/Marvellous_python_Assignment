import multiprocessing.process
import time
import os 
import multiprocessing

def Square(no):
    squar=[]
    for i in no:
        Squa=i*i
        squar.append(Squa)
    print(squar)
        



def main():
    n=int(input("Enter size of list:"))
    data=[]
    for i in range(n):
        no=int(input())
        data.append(no)

    print(data)

    p=multiprocessing.Process(target=Square,args=(data,))
    p.start()
    p.join()



if __name__=="__main__":
    main()