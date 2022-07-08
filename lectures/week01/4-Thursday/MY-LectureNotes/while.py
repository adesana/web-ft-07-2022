
#1. Create a program that will print from 1-10 using a while loop.

#2. Create a program that will print from 10-1 using a while loop.

#3. Create a program that prompts the user to enter a word.  The program doesn't stop asking the user to enter a word until the user enters the word "stop"

#4a. Create a program that has a variable named username and another variabled named password with values of your choice.

#4b. Prompt the user for a username and then a password.

#4c. If the both match continue on with the program and give a welcome message.

#4d. If not it prompts the user for the username and password until they get it correct.

#4e. (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.


#1
i = 1
while(i<=10):
    print(i)
    i+=1

#2
i = 10
while(i>=1):
    print(i)
    i-=1

#3
answer = input('Enter a word:   ')
while answer != 'Stop':
    answer = input('Enter a word:   ')


#4

saved_username = 'adesana'
saved_password = '1234'
username = ''
password = ''
attempts = 0
#4b


while username != saved_username or password != saved_password:
    username = input('Enter your username:   ')
    password = input('Enter your password:   ')
    attempts+=1

    if attempts > 5:
        print('You failed, restart the program.')
        
    if username == saved_username and password == saved_password:
        print('Welcome!')


