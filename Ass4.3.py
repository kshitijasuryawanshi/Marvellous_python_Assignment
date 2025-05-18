from functools import reduce

def Check(No):
    if((No>=70) and(No<=90)):
        return No
    
def Increase(No):
     return No+10

def Product(A,B):
    return A*B
    

def main():
    size=int(input("Enter number of elements in list:"))

    data=[]
    print("please enter elements in list:")
    for i in range(size):
        no=int(input())
        data.append(no)


    print("Input data",data)

    FData=list(filter(Check,data))
    print("filter output:",FData)

    MData=list(map(Increase,FData))
    print("map output:",MData)

    
    RData=reduce(Product,MData)
    print("reduce output:",RData)


if __name__=="__main__":
    main()