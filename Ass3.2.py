no=int(input("Enter size of list:"))

data=list()

print("Please enter values in list:")

for i in range(no):
    j=int(input())
    data.append(j)


print("Entered list is:",data)

max=data[0]
for i in range(1,no):
    if(max<data[i]):
        max=data[i]


print("Maximum value in list is:",max)