
i=1
def Display(n):
    global i
    if(n>=1):
        for j in range(0,i):
            print("*",end=" ")
        i=i+1
        n=n-1
        print(end="\n")
        Display(n)


def main():
    ret=Display(4)
    print(ret)

if __name__=="__main__":
    main()