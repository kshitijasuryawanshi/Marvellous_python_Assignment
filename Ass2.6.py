no=int(input("Enter number"))

for i in range(no,0,-1):
    for j in range(i):
        print("*",end="\t")
    print(end="\n")