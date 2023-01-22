#Made By Vivek

Year=int(input("Enter a Year: "))

if (Year%4==0) and (Year%100!=0):
    print(Year,"Is a leap year")

elif (Year%400==0) and (Year%100==0):
    print(Year,"Is a leap year")

else:
    print(Year,"Is not a leap year")
