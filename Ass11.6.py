sum=0
count=1
def Display(n):
    global sum
    global count
    if (n>=1):
        sum=sum+count
        count=count+1
        n=n-1
        Display(n)
    return sum



def main():
    ret=Display(4)
    print(ret)




if __name__=="__main__":
    main()