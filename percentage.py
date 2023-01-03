print("•Select *(1)* if you want ur percentage out of 40 in all subjects excluding Ai..")
print("\n••And select *(2)* if you want ur percentage out of 80 in all subjects excluding Ai.. \n")
print("------------------------------------------------------")

m=int(input("   ••Choose: "))

if m == 1:
    a= int(input("Enter your marks of Maths out of 40: "))
    b= int(input("Enter your marks of Science out of 40: "))
    c= int(input("Enter your marks of Hindi out of 40: "))
    d= int(input("Enter your marks of SST out of 40: "))
    e= int(input("Enter your marks of English out of 40: "))
    x= (a+b+c+d+e)
    
    z= (x/200)*100
    
    print("So your percentage is: ",z)

else:
    a= int(input("Enter your marks of Maths oit of 80: "))
    b= int(input("Enter your marks of Science out of 80: "))
    c= int(input("Enter your marks of Hindi out of 80: "))
    d= int(input("Enter your marks of SST out or 80: "))
    e= int(input("Enter your marks of English out of 80: "))
    
    x= (a+b+c+d+e)
    
    z= (x/400)*100
    
    print("So your percentage is: ",z)