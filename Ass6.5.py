

def main():
    no=int(input("Enter number:"))

    if(no<0):
        print("number is not prime")
    elif(no==1 or no==2):
        print("Number is prime")
    else:
        for i in range(2,no):
            if(no%i==0):
                print("number is not prime")
        print("Number is prime")


if __name__=="__main__":
    main()