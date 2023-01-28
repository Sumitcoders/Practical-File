#WAP to compare no.s on the basis of greater or smaller ..

x = int(input("Enter the 1st number : "))
y = int(input("Enter 2nd number : "))

if x>y:
    print(">>",x,"is greater than",y)
    print(">>And",y,"is smaller than",x)
    
elif x==y:
    print("Both the numbers are equal..")
    
else:
    print(">>",y,"is greater than ",x)
    print(">>And",x,"is smaller than",y)