# Made by @Sumitcoders
#wap a code to find the average of the number given by the user

t = int(input('Enter the total count of the numbers: '))
sum = 0
for i in range(t):
    no = float(input(f'Enter the number {i+1}: '))
    sum = sum + no
avg = sum/t
print((avg), f' is the average of the above {t} numbers')
input('Press ENTER to exit')
