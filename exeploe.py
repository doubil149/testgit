#attendes=['yassir','hamza','bilal']
attende=input('enter the names of attendees separated by commas:')
attendes=[]
confirmed=[]
not_confirmed=[]
attendes=attende.split(',')
for person in attendes:
    print(person)
    yes_no=input(f'is {person} attending?(yes or no)').lower()
    if yes_no=='no':
      print('attendance not confirmed')
      not_confirmed.append(person)
    else:
      print('attendance confirmed')
      confirmed.append(person)
    print('------')
attend=input('do you want to see your list? (yes or no)').lower()
if attend=='yes':
   print(confirmed)
   print(not_confirmed)

   
