while True:    
    import random

    print (" \n Welcome to Coin flip Game. \n")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    print("         You just have to predict.. \n That when we toss a coin which side will come.. ")
    print("                         -copyrights of the Game belongs to \n                            ••| Badal °_° |•• ")
    print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
    choice = input("Enter your choice (Heads or tails ) : ")
    
    num = random.randint(1,2)
        
    if num==1:
        result= "heads"
            
    elif num==2:
        result="tails"
        
    if choice== result:
        print("••••••••••••••••••••••••••••••••••••••••••••\n Good job..! You Guessed it right..\n The coin flipped ==>",result)
        print("•••••••••••••••••••••••••••••••••••••••••••••")
    else:        #choice != result 
        print("••••••••••••••••••••••••••••••••••• \n ohh no..you guessed it wrong ..\n The coin flipped ==>" ,result)
        print("•••••••••••••••••••••••••••••••••••••••• \n ")
        
    input("Want to Play again hit Enter..")