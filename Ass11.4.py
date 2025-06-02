power=1
def Display(n,m):
    global power
    if(m>=1):
        power=power*n
        m=m-1
        Display(n,m)
    return power
        
def main():
    ret=Display(2,3)
    print(ret)

if __name__=="__main__":
    main()