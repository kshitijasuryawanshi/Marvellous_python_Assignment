import  MarvellousNum

sum=0
def ListPrime(value):
    global sum
    if(MarvellousNum.checkPrime(value)==True):
        sum=sum+value


def main():
    no=int(input("Enter number of elements in list"))
    data=list()

    print("please enter elements in list:")
    for i in range(no):
        j=int(input())
        data.append(j)
    
    for i in range(len(data)):
        ListPrime(data[i])
    
    print("Addition of prime numbers is:",sum)
    


if __name__=="__main__":
    main()