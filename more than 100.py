while True:
    try:
        a = int(input("Enter "))
    except ValueError:
        print("invalid input")
        continue
        
    else:
        break
        
if a>100:
    print("the num is more than")
    
else:
    print("less than")
    