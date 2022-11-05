print('Welcome to the age finder')
B_d = input('Enter your birth date (i.e 04/06/2007) : ')
if len(str(B_d)) == 10:
    pass
else:
    print('Invalid format')
    exit()







c_d = input('Enter the current date (i.e 10/10/2022) : ')

if len(str(c_d)) == 10:
    pass
else:
    print('Invalid format')
    exit()



date = B_d[0:2]

month = B_d[3:5]

year = B_d[6:10]

c_date = c_d[0:2]

c_month = c_d[3:5]

c_year = c_d[6:10]

if int(date) > 31 or int(date) < 0:
    exit('invalid date')

if int(date) == 31:
    if month != 1 and month != 3 and month != 5 and month != 7 and month != 9 and month != 11:
        exit('invalid date')
    else:
        pass
if int(month) < 0 or int(month) > 12:
    exit('invalid month')
if int(c_year) < int(year):
    exit('invalid Year')
if int(month) == 2:
    if int(date) == 29:
        if (int(year)/4) == (int(year)//4):
            pass
        else:
            exit('invalid date')
if int(c_month) == 2:
    if int(c_date) == 29:
        if (int(c_year)/4) == (int(c_year)//4):
            pass
        else:
            exit('invalid date')






if int(c_date) >= int(date):
    a_date = int(c_date) - int(date)
    if int(month) <= int(c_month):
        a_month = int(c_month) - int(month)
        a_year = int(c_year) - int(year)
    elif int(month) >= int(c_month):
        a_month = 12 - (int(month) - int(c_month))
        a_year = int(int(c_year) - int(year)) - 1

elif int(c_date) < int(date):
    if int(c_month) == 1 or int(c_month) == 5 or int(c_month) == 7 or int(c_month) == 9 or int(c_month) == 11:
        a_date = 30 - (int(date) - int(c_date))
    if int(c_month) == 4 or int(c_month) == 6 or int(c_month) == 8 or int(c_month) == 10 or int(c_month) == 12 or int(c_month) == 2:
        a_date = 31 - (int(date) - int(c_date))
    else:
        if (int(c_year)/4) == int(int(c_year)//4):
            a_date = 29 - (int(date) - int(c_date))
        else:
            a_date = 28 - (int(date) - int(c_date))
    
    if int(month) < int(c_month):
        a_month = int(c_month) - int(month)
        a_year = int(c_year) - int(year)
    elif int(month) >= int(c_month):
        a_month = 12 - (int(month) - int(c_month))
        a_year = int(int(c_year) - int(year)) - 1

print(f"You are {a_year} years, {a_month} months and {a_date} days.")




