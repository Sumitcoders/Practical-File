#Design
p_1="====================================================="
p_2="=============================="

#Main body
print(p_1)
print("\tWelcome To Driving School Online Portal")
print(p_1)
name=input("Enter your name -to continue further: ")
print(p_1)
print("Hello",name.capitalize())
print(p_2)
a = int(input("Enter Your Age: "))
print(p_2)
if a>=7 and a <= 100:
 if a > 18:
   print(name.capitalize(),",You Are Eligible to Drive")
   print(p_2)
 elif a==18:
    print(name.capitalize(),",It Can't be Decided. Please Come To The Office Physically")
    print(p_2)
 elif a<18:
    print(name.capitalize(),",You Are Not Eligible To Drive")
    print(p_2)
else:
    print(name.capitalize(),",You Do Not Enter Logical Age to Drive")
    print(p_2)
print("Thank You To Visit Our Portal",name.capitalize())
print(p_1)
