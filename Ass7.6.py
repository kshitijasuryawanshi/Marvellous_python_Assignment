from functools import reduce 

def Prime(No):
    if(No==1 or No==2):
        return No
    else:
        for i in range(2,No):
            if(No%i!=0):
               break
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

    FData=list(filter(Prime,Data))
    print("map output:",FData)


if __name__=="__main__":
    main()

