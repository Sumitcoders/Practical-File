import time
import sys

#variables

l_1 =  "----------------------------------------------"
l_2= "--------------------------------------------------------------------------------------"

#Welcome Screen
print("Welcome User ;)")
print("")
print("")
print("Following are the instructions to use")
print("""
1. From the basic form of Quadratic Equation (ax² + bx + c) , you will be asked for the value of coefficients of variables i.e. the value of (a) and (b).
2. Then you will be asked for the constant term (c)
2. That's it! Enter those values and you will get your roots/zeroes of equation!!
""")
print("")
print("")
while True:
  print("Press 1 to start")
  strt = int(input("=>"))
  if strt ==1:
    print(l_2)
    print("Enter the value of coefficient of x²")
    a = int(input("=>"))
    print("Enter the value of coefficient of x")
    b = int(input("=>"))
    print("Enter the value of constant term")
    c = int(input("=>"))
    
    print("")
    print("Your equation is:")
    print(l_1)
    print(f"{a}x² + {b}x + {c}")
    print(l_1)
    print("Zeroes of your equation is:")
    a2 = (1/a)*a
    b2 = (1/a)*b
    c2 = (1/a)*c
    D = b2*b2 - 4*a2*c2
    z_1 = (-b2 + D**0.5)/2*a2
    z_2 = (-b2 - D**0.5)/2*a2
    print("Zeroes of your equation are:")
    print(f"1. {z_1}")
    print(f"2. {z_2}")
    print("Thanks for using . Have a nice day :)")
    print(l_2)
    break
  else:
    print ("Please provide a valid option")
    continue
