print('welcome to place the rabbit')
field=[[1 ,2 ,3 ],[1 ,2 ,3 ],[1 ,2 ,3 ]]
print(f'{field[0]}\n{field[1]}\n{field[2]}')
print('\n where should the rabbit go? 5')
position=input('please choose a row and colomn')
row=int(position[0])
column=int(position[1])
field[row-1][column-1] ='0'
print('\n Success...\n')
print(f'{field[0]}\n{field[1]}\n{field[2]}')