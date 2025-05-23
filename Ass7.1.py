
Square=lambda X:X*X

cube=lambda X : X*X*X


def main():
   n=int(input("Enter number:"))
   iRet=Square(n)
   print("Square:",iRet)
   iRet=cube(n)
   print("Cube is:",iRet)


if __name__=="__main__":
    main()