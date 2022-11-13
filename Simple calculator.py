print("\t\tWelcome to Simple Calculator")

num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the sencond number: "))
opt =input("Enter the operation: ")

if opt=="+":
    print("Your Answer is", num1+num2)

if opt=="-":
    print("Your Answer is", num1-num2)

if opt=="*":
    print("Your Answer is", num1*num2)

if opt=="/":
    print("Your Answer is", num1/num2)

if opt=="**":
    print("Your Answer is", num1**num2)

print("Thank you for using simple calculator")




