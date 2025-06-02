fact=1
def Display(n):
    global fact
    if(n>=1):
        fact=fact*n
        n=n-1
        Display(n)
    return fact
        
def main():
    ret=Display(5)
    print(ret)

if __name__=="__main__":
    main()