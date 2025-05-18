from functools import reduce

def Prime(No):
    for i in range(2,No):
        if No%i==0 :
            break
        return No
        
    
def Multiply(No):
     return No*2

def Sum(A,B):
    max=A
    if(B>max):
        max=B
    return max
    

def main():
    size=int(input("Enter number of elements in list:"))

    data=[]
    print("please enter elements in list:")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("Input data",data)

    FData=list(filter(Prime,data))
    print("filter output:",FData)

    MData=list(map(Multiply,FData))
    print("map output:",MData)

    
    RData=reduce(Sum,MData)
    print("reduce output:",RData)


if __name__=="__main__":
    main()