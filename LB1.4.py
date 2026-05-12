
def main():
    i=int(input("enter the number the check it is divisible by 5 or not: "))
    print(f"{i}")
    result=i/5
    if(result==0):
        return True
    else:
        return False
         



if __name__=="__main__":

    iRet=main()
    if(iRet==True):
        print("number is divisible by 5")
    else:
        print("number is not divisible by 5")