
def Divisble(value):
    if(value%5==0):
        return True
    else:
        return False
    
def main():
    no=int(input("Enter number:"))

    result=Divisble(no)
    print(result)




if __name__=="__main__":
    main()