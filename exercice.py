import random
print('welcome to -whose wallet-')
print('u will give a list of nammes ,and i will pick a person o pay')
names=input(' if u r  ready enter names separated by comma:\n').split(", ")

print(f"please ask {random.choice(names)} to take his wallet out")
