own1=input('enter the name of a book you own:\n')
ur_own=[]
ur_futur=[]
if own1:
    own2=input('enter the name of another book you own( or press -enter- to skip):\n')
    if own2:
        ur_own.append(own1)
        ur_own.append(own2)
        print(f'your library:{ur_own}')
    else:
        ur_own.append(own1)
        print(f'your library:{ur_own}')
else:
    print(f'your library:{ur_own}')
futur1=input('enter name of a book you wish to have in the futures:\n')
if futur1:
    futur2=input('enter name of another book you wish to have in the futures ( or press -enter- to skip):\n')
    if futur2:
        ur_futur.append(futur1)
        ur_futur.append(futur2)
        print(f'your wish list:{ur_futur}')
    else:
        ur_futur.append(futur1)
        print(f'your library:{ur_futur}')
else:
     print(f'your wish list:{ur_futur}')
own3=input('enter the name of a book from ur futur list you have it ( or press -enter- to skip):\n')
if own3 in ur_futur:
   ur_own.append(own3)
   ur_futur.remove(own3)
   print('ur updated list is:',ur_own)
   print('ur updated wishslist is:',ur_futur)
donated_book=input('enter name from ur library you wish todonate\n')
if donated_book in ur_own: 
    ur_own.remove(donated_book)
    print(f'ur final list is {ur_own}')



