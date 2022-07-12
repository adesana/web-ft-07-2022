# Homework 7/12

import pickle

try:
    with open('phonebook.pickle', 'rb') as fh:
        phonebook = pickle.load(fh)
except:
    phonebook = {}

def welcome():
    main_menu = int(input("""
    Electronic Phone Book
    =====================
    What would you like to do?
    1. Look up a contact.
    2. Create a new contact.
    3. Delete a contact.
    4. List all contacts.
    5. Quit.
    
    Please choose an option 1-5.           """))
    return main_menu



def contact():    

    while True:
        entry = welcome()
        if entry == 1:
            name = input('Enter the name of the contact details you wish to view.         ')
            if name in phonebook:
                print(f'The contact is {name} : {phonebook[name]}')
            else:
                print('That contact does not exist, return to the main menu for entry.        ')
        elif entry == 2:
            contact_name = input('What is the name of the contact?      ')
            phone_number = input('Please enter the phone number of the contact.         ')
            if phone_number not in phonebook.items():
                phonebook.update({contact_name:phone_number})
                print('Contact has been successfully saved.           ')
                print(f'{contact_name} : {phone_number}')
            else:
                print('That contact already exists in your phonebook.        ')
        elif entry == 3:
            name = input('Enter the name of the contact you wish to delete.      ')
            if name in phonebook:
                print(f'The contact name is {name} : {phonebook[name]}')
                confirm = input('Is this the contact you wish to delete? Yes or No       ')
            else:
                print('That contact does not exist, return to the main menu.          ')
                      
            if confirm.capitalize() == 'Yes':
                del phonebook[name]
            else:
                print('Return to main menu.       ')
        elif entry == 4:
            if bool(phonebook) != False:
                for x, y, in phonebook.items():
                    print(x, '-->', y)
            else:
                print('Your phonebook is empty, return to the main menu to add a contact.        ')
        elif entry == 5:
            print('Thank you, goodbye.              ')
            with open('phonebook.pickle', 'wb') as fh:
                pickle.dump(phonebook, fh)
            break
        else:
            print('Incorrect Entry.        ')
        


contact()




