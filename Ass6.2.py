

def main():
    #######################################################################
    sum=0
    for i in range(1,101):
        if(i%2==0):
            sum=sum+i
    print("Sum of Even Numbers between 1 to 100 :",sum)
    #######################################################################
    #### code using while####
    i=1
    sum=0
    while(i<=100):
        if(i%2==0):
            sum=sum+i
        i=i+1

    print("Sum of even numbers between 1 to 100 is :",sum)


if __name__=="__main__":
    main()