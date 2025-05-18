no=int(input("Enter the size of list:"))

data=list()


print("please enter values in list:")
for i in range(no):
    j=int(input())
    data.append(j)

min=data[0]

for i in range(1,no):
    if(min>data[i]):
        min=data[i]


print("Minimum value in list is:",min)