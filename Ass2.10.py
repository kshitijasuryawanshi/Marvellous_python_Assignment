no=int(input("Enter number:"))

no=str(no)
sum=0
for i in range(len(no)):
    sum=sum+int(no[i])
print("sum of digits is:",sum)