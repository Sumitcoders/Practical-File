print("Welcome To Driving School Online Portal")
a = int(input("Enter Your Age: "))
if a>=7 and a <= 100:
 if a > 18:
    print("You Are Eligible to Drive")
 elif a==18:
    print("Can't be Decided. Please Come To The Office Physically")
 elif a<18:
    print("You Are Not Eligible To Drive")
else:
    print("You Do Not Enter Logical Age to Drive")

print("Thank You To Visit Our Portal")
