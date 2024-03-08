city=input('choisir une ville: rabat, casablnca or tanger\n')
if city.upper()=='RABAT' or city.lower()=='casablnca' or city.lower()=='tanger':
    print(f'welcom {city} is on our list!')
else:
    print(f'sorry {city} isnt on our list!')