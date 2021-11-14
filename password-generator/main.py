# simple password generator in python
import random

print("Welcome to the password generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

number = input('Amount of passwords to generate: ')
number  = int(number)

length = input("Please enter the length of your password: ")
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)