no=int(input("enter size of list:"))

data=list()

print("please enter values in list:")

for i in range(no):
    j=int(input())
    data.append(j)

freq=int(input("Please enter number for finding frequency :"))

count=0
for i in range(len(data)):
    if(data[i]==freq):
        count=count+1
    
print("Frequency of enter number is:",count)
