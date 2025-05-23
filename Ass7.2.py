from functools import reduce 

def double(No):
    return No*2

def main():
    Data=[]

    print("Enter number of elements:")
    Size=int(input())

    print("Please enter number values :")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input data:",Data)

    MData=list(map(double,Data))
    print("map output:",MData)


if __name__=="__main__":
    main()

