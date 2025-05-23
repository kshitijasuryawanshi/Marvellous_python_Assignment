

def main():
    #######################################################################
    print("Enter 5 number:")
    no1=int(input())
    no2=int(input())
    no3=int(input())
    no4=int(input())
    no5=int(input())

    larger=no1
    for i in range(0,5):
        if(no2>larger):
            larger=no2
        elif(no3>larger):
            larger=no3
        elif(no4>larger):
            larger=no4 
        elif(no5>larger):
            larger=no5
    print("Larger Number is:",larger)    


if __name__=="__main__":
    main()