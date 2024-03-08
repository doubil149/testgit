print('welcome to the coin guessing game!')
print('choose a method to toss the coin:\n')
print(''' 1.using random.random()
 2.using random.randint   
      ''')
import random
mbr=random.random()
nbr=random.randint(0,1)
choose=int(input('enter your choice (1 or 2)\n'))
if choose==1:
    if mbr>=0.5:
      computer='head'
    else:
      computer='king'
elif choose==2:
    if nbr==0:
       computer='head'
    else:
       computer='king'
else:
   print('choisi 1 ou 2')
guess=input('enter ur guess (head or king):\n')
if guess.lower()==computer.lower():
   print("u won")
else:
   print('u lost')
print(f'the computer result is {computer}')   
