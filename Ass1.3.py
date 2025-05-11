

def Addition(value1,value2):
    Ans=0
    Ans=value1+value2
    return Ans

def main():
    no1=int(input("Enter First number:"))
    no2=int(input("Enter second number:"))

    result=Addition(no1,no2)
    print("Addition of two numbers",result)





if __name__=="__main__":
    main()