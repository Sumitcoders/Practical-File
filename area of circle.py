print(" Please choose from these...")
print("    •Yes")
print("    •No")
print("                         ")

#space is given o4qA⁰n line 2 and 5.. 

dep= input("  •Do you want to use the value of π in decimal ??(yes/no) :")

if dep.capitalize()=="Yes" :
    print("π = 3.14")
    x = 3.14
    r = float(input("Enter the Radius of the Circle: "))
    area = x*(r**2)
    print("The Area of the Circle is:",area)
    
elif dep.capitalize()=="No" :
    print("π = 22/7")
    pie = 22/7
    r = float(input("Enter the Radius of the Circle: "))
    area = float(pie)*float(r)*float(r)
    print("The Area of the Circle is:",area)
    
else :
    print ("invalid input")
