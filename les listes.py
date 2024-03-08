color1=input('add the first color you like:\n')
chose=input('do you want to add more colors? yes or no?\n')
colors=[]
if chose.lower()=='yes':
     color2=input(' add another colors?\n')
     colors.append(color1)
     colors.append(color2)
     print(f'the colors u like are: {colors}')
else :
     colors.append(color1)
     print(f'the color u like is: {colors}')


