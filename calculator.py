#Made by Divyansh
#WAP to make a function calculator

def cal(first, second, opreation):
    if opreation == 't1' or opreation == 'sum':
        result=first+second   
    elif opreation == 't2' or opreation == 'sub':
        result=first-second
    elif opreation == 't3' or opreation == 'multi':
        result=first*second  
    elif opreation == 't4' or opreation == 'divi':
        result=first/second 
    elif opreation == 't5' or opreation == 'table':
        result = (f'''
                 {firstnum} x 1 = {firstnum} 
                 {firstnum} x 2 = {firstnum*2}
                 {firstnum} x 3 = {firstnum*3}
                 {firstnum} x 4 = {firstnum*4}
                 {firstnum} x 5 = {firstnum*5}
                 {firstnum} x 6 = {firstnum*6}
                 {firstnum} x 7 = {firstnum*7}
                 {firstnum} x 8 = {firstnum*8}
                 {firstnum} x 9 = {firstnum*9}
                 {firstnum} x 10 = {firstnum*10}
                 ''')     
    else:
        print('It seems that there is a mistake in calculator or you have enter some thing worng')       
    print(f"THE RESULT IS: {result}")    

firstnum = int(input("Enter the first digit: "))
secondnum = int(input("Enter the second digit: "))
print('''
        Type 't1' or 'sum' to find the sum of two given number;
        Type 't2' or 'sub' to find the subtraction of two given number;
        Type 't3' or 'multi' to find the multiplication of two given number;
        Type 't4' or 'divi' to find the division of two given number;
        Type 't5' or 'table' to find the table of given number (Enter any number in second number)
        ''')
find = input("Enter the opreation type: ")


cal(firstnum, secondnum, find) 


#run and execute the code.
