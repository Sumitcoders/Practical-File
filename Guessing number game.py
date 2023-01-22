import random
#design
p1="================================================="
n=random.randint(0,20)

number_of_guesses = 1
print(p1)
print("This is the game of guessing number")
print("there are only 12 guesses so please think gently")
print(p1)

while(number_of_guesses<=6):
    guess_number=int(input("Enter the number "))
    print(p1)
    if guess_number>n:
        print("You entered greater number write smaller number\n")
        print(p1)
    elif guess_number<n:
        print("You entered less number write greater number\n")
        print(p1)
    else:
        print("You Won Congratulations\n")
        print(number_of_guesses,"Number of guesses you took to finish")
        print(p1)
        break
    print(6 - number_of_guesses, """no. of guesses left""")
    print(p1)
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 6):
    print("Game Over")
    print("The number is: ", n)
    print(p1)
