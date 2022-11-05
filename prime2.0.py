#Program to input any number from user
#Check it is Prime number of not
n = int(input("Enter a number: "))
x = False
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            x = True
            break
if x:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")