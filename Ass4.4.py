from functools import reduce

def Even(No):
    if((No>=70) and(No<=90)):
        return No
    
def Square(No):
     return No*No

def Sum(A,B):
    return A+B
    

def main():
    size=int(input("Enter number of elements in list:"))

    data=[]
    print("please enter elements in list:")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("Input data",data)

    FData=list(filter(Even,data))
    print("filter output:",FData)

    MData=list(map(Square,FData))
    print("map output:",MData)

    
    RData=reduce(Sum,MData)
    print("reduce output:",RData)


if __name__=="__main__":
    main()