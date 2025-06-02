count=0
def Display(n):
    global count
    digit=0
    if(n>=1):
        digit=n%10
        if(digit==0):
            count=count+1
        n=n//10
        Display(n)
    return count
        
def main():
    ret=Display(100045301)
    print(ret)

if __name__=="__main__":
    main()