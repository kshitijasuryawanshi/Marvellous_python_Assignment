def main():
    
    n=int(input("Enter Number:"))
    fact=n
    for i in range(1,n):
        fact=fact*i
    print("factorial of number is:",fact)


if __name__=="__main__":
    main()