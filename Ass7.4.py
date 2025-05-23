from functools import reduce 

def product(A,B):
    return A*B
    

def main():
    Data=[]

    print("Enter number of elements:")
    Size=int(input())

    print("Please enter number values :")
    for i in range(Size):
        no=int(input())
        Data.append(no)

    print("Input data:",Data)

    RData=list(reduce(product,Data))
    print("reduce output:",RData)


if __name__=="__main__":
    main()

