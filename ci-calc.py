#Made by Divyansh
#WAP to find Compound Interest with net Amount

print('Compund Interest Calculation:')
P = float(input('Pincipal?'))
R = float(input('Rate of interest?'))
T = float(input('Duration (No. of years)?'))

Amount = (P*pow(1 + (R/100),T))
Interest = Amount-P
print('/nInterest = %0.2f'%Interest)

#run and execute the code.
