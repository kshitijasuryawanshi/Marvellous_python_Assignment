from functools import reduce 

def Even(No):
    if(No%2==0):
        return No

def main():
    Data=[]

    print("Enter number of elements:")
    Size=int(input())

    print("Please enter number values :")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input data:",Data)

    FData=list(filter(Even,Data))
    print("map output:",FData)


if __name__=="__main__":
    main()

