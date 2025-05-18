no=int(input("Enter number:"))

sum=0
for i in range(1,no):
    if(no%i==0):
        sum=sum+i

print("Addition of factors :",sum)


