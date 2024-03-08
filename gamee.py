import random
pin=random.randint(1000,9999)
user_inp=int(input("enrer 4 digits pin code :\n"))
if len(str(user_inp)) !=4:
    print('plz entrer 4 digits\n')
elif user_inp==pin:
    print('le code est corr')
else:
    print('le code est incorrect')
    print(f'the computer generate this code {pin}')