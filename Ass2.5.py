no = int(input("Enter number:"))

if no <= 1:
    print("Number is not prime")
elif no == 2:
    print("Prime number")
else:
    is_prime = True
    for i in range(2, no):
        if no % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Number is not prime")
