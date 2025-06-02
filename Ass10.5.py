
def isPrime(No):
    if(No<=1):
        return False
    for  i in range(2,int((No**0.5))+1):
        if(No%i==0):
            return False
    return True

def Mult(No):
    return No*2

def Max(A,B):
    if (A>B):
        return A
    else:
        return B

def filterX(Task,Values):
    Result=[]

    for no in Values:
        ret=Task(no)
        if(ret==True):
            Result.append(no)
    return Result

def mapX(Task,Values):
    Result=[]

    for no in Values:
        ret=Task(no)
        Result.append(ret)
    return Result

def reduceX(Task,Values):
    Result=0

    for no in Values:
        Result=Task(Result,no)

    return Result
    
def main():
    n=int(input("Enter Size of list:"))


    data=[]
    for i in range(n):
        no=int(input())
        data.append(no)

    print(data)

    FData=list(filterX(isPrime,data))
    print("Filter data:",FData)

    MData=list(mapX(Mult,FData))
    print("MData is :",MData)

    RData=reduceX(Max,MData)
    print("Reduce data :",RData)

if __name__=="__main__":
    main()