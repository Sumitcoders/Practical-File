import time

B = '\ '

print(f'''
  WELCOME TO THE HYDROCARBON PYTHON PROGRAMM

  H H H H H                        H H H                                                       
  | | | | |                        | | |                                                           
H-C-C-C-C=C                      C≡C-C-C-H
  | | | | |                     /  | | |
  H H H H H                    OH  H H H                                                          
                        H
                       /   
            H H H H   C-H
            | | | |  / {B}
          H-C-C-C-C=C   H
            | | | |  {B}
            H H H H  H-C-H
                       |
                       H




''')
carbon = int(input('No. of carbon in the compound: '))
hydrogen = int(input('NO. of hydrogen in the compound: '))

 
if carbon == 0:
    exit()


compound = 'C' + str(carbon) + 'H' + str(hydrogen)
print('your compound is ',compound)
print('checking for a valid hydrocarbon compound...')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1)
if (hydrogen - 2)/2 == carbon:
    print('Its an alkane')
elif hydrogen / 2 == carbon:
    print('Its an alkene')
elif (hydrogen + 2) / 2 == carbon:
    print('Its an alkyne ')
else:
    print('Invalid hydrocarbon')   

input('press ENTER to exit')