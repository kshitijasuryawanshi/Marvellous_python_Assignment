i=1
def Display(n):
    global i
    if(n>=1):
        print(i,end=" ")
        n=n-1
        i=i+1
        Display(n)
        
def main():
    Display(5)

if __name__=="__main__":
    main()