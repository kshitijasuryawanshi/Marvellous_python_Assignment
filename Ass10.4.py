
def checkEven(No):
    if(No%2==0):
        return True
    
def Square(No):
    return No*No

def Sum(A,B):
    return A+B


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

    n=int(input("enter size of list:"))

    data =[]
    for i in range(n):
        no=int(input())
        data.append(no)

    print(data)

    FData=list(filterX(checkEven,data))
    print("filter data:",FData)


    MData=list(mapX(Square,FData))
    print("map data:",MData)

    RData=reduceX(Sum,MData)
    print("Sum data:",RData)


if __name__=="__main__":
    main()