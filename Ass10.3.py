
def CheckNum(No):
    if(No>=70 and No<=90):
        return True

def Increase(n):
    return n+10

def Product(A,B):
    return A*B


def filterX(Task,Values):
    Result=[]

    for no in Values:
        ret=Task(no)
        if (ret==True):
            Result.append(no)
    return Result

def mapX(Task,Values):
    Result=[]

    for no in Values:
        ret=Task(no)
        Result.append(ret)

    return Result


def reduceX(Task,Values):
    Result=1

    for no in Values:
        Result=Task(Result,no)
    
    return Result



def main():
    n=int(input("Enter size:"))

    data=[]
    for i in range(n):
        No=int(input())
        data.append(No)
    print(data)

    FData=list(filterX(CheckNum,data))
    print("filter output:",FData)

    MData=list(mapX(Increase,FData))
    print("map output:",MData)

    RData=reduceX(Product,MData)
    print("reduce output:",RData)



if __name__=="__main__":
    main()