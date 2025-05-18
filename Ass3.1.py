no=int(input("Enter size of list:"))

data=list()
print("Please enter value in list")

for i in range(no):
    value=int(input())
    data.append(value)


print(data)

sum=0
for i in range(no):
    sum=sum+data[i]

print("Addition of elemnet in list is:",sum)