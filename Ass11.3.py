Sum=0
def Display(n):
    global Sum
    digit=0
    if(n>=1):
        digit=n%10
        Sum=Sum+digit
        n=n//10
        Display(n)
    return Sum
        
def main():
    ret=Display(1234)
    print(ret)


if __name__=="__main__":
    main()