print('WELCOME TO THE QUADRATIC EQUATION ROOT FINDER!')



a = int(input('Enter the Coefficient of x²: '))
b = int(input('Enter the Coefficient of x: '))
c = int(input('Enter the constant: '))

print(('OK..'),end='')
print('I chatch the below equation from your inputs')
equation = str(a) + 'x²'
if b < 0:
    equation = equation + str(b) + 'x'
else:
    equation = equation + '+' + str(b) + 'x'
if c < 0:
    equation = equation + str(c)
else:
    equation = equation + '+' + str(c)


print(equation)

D = b**2 - 4*a*c

x1,x2 = (-b + D**0.5)/(2*a),(-b - D**0.5)/(2*a)
print('so the zeroes of this equation are :- ',x1,' and ', x2)
