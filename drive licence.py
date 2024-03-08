print('welcome\n')
age=int(input('enter ur age\n'))
if age>=18:
    choise=input('do u have a driver licence entrer yes or no \n')
    
    if choise.lower()=='yes':
        print('u can drive\n')
    else:
        print('u cant drive\n')
else:
    print('u cant drive')