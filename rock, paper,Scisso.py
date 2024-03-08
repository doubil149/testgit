import random
print('welcome to the rock, paper,Scissors game:')
choose=input('press enter to continue or type -Help- for the rules help\n').lower()
if choose=='help':
    print('''
                    *****RULES*****
          1) you choose and the computer chooses
          2) rock smashes scissors-> rock win
          3) scissors cut paper-> scissors win 
          4) paper covers rock -> paper win
          ''')
game=['rock','paper','scissors']
my_choice=input('enter ur choice (rock,paper,scissors)\n').lower()
if my_choice not in ['rock','paper','scissors']:
    print('invalid choice')


