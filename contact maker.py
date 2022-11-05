# There should be an empty folder named 'contacts' in the same directry for this application to work


import os
import random
import time
def num_check(number):
    if len(str(number)) == 10:
        pass
    else:
        print('type a valid number')
        exit()

def add_contact(name,number):
    l = os.listdir('contacts')
    name_a = name + '.txt'
    a = True
    for i in range(len(l)):
        if l[i] == name_a:
            print('contact already exist! Do you want to over write it?')
            y = input('(y/n): ')
            if y != 'y':
                a = False
            else:
                a = True
    if a != False:

        file = 'contacts/' + name + '.txt'
        f = open(file, 'w')
        f.write(f'{name} : {number}')
        f.close()
        print('Contact added succesfully!')

def list_contact():
    contacts = os.listdir('contacts')
    for i in range(len(contacts)):
        a = len(contacts[i])-4
        b = contacts[i]
        print(b[0:a])
    input('press Enter to exit ')
def find(name):
    try:
        name = 'contacts/' + name + '.txt'
        f = open(name)
        co = f.read()
        input('Press Enter to view contact ')
        print(co)
        input('press Enter to exit ')
        

        
    except:
        print('no such contact exist')

    
        
print('welcom to the contact maker')
def main():
    print('press 1 to add any contact \npress 2 for viewing the contact list \npress 3 for finding the contact')
    i = int(input('enter your choice: '))
    if i == 1:
        c = input('Type the name of the contact: ')
        no = int(input('Type the number of the contact: '))
        num_check(no)
        add_contact(c,no)

    elif i == 2:
        list_contact()
    elif i == 3:
        i = input('Enter the contact name: ')
        find(i)
    elif i == 4:
        i = input('Type the name of the contact to remove : ')
        print('Are you sure to remove this contact? i.e ' + str(i))
        y = input('(y/n) ')
        if y != 'y':
            exit()
        else:
            pat = 'contacts/' + str(i) + '.txt'
            try:
                os.remove(pat)
            except:
                print('No such contact to remove')
                input('press enter to exit')
                exit()
            time.sleep(1)
            print('Removing ...')
            time.sleep(random.randint(0,2))
            print('..')
            time.sleep(random.randint(0,2))
            print('..')
            time.sleep(1)
            print('Succesfully removed ' + str(i))
            input('press enter to exit')
            
        

main()
