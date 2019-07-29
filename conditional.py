#input
user_id = input('what is your id?')
userInput = input('what is your password?')

#if statement
'''
if userInput == '111111':
    print("The user password is authorized")
else:
    print("Try Again")

if user_id == 'kyu':
    if userInput == '111111':
        print("The user is authorized")
    else:
        print("Invalid password")
else:
    print("Invalid ID")
'''

#Logical operator
if user_id == 'kyu' and userInput == '111111':
    print("The user is authorized")
elif user_id == 'rey' and userInput == '222222':
    print("The user is authorized")
else:
    print("Invalid user")
