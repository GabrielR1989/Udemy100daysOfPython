import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

initial_password = ""
initial_password_backup = ""
index_initial_password = 0
final_password = ""

#Randomly select the characters from the lists: letters, numbers, symbols with the parameters entered by the user
for i in range(nr_letters):
    initial_password += random.choice(letters)

for i in range(nr_numbers):
    initial_password += random.choice(numbers)

for i in range(nr_symbols):
    initial_password += random.choice(symbols)
#------------------------------------------------------------------------------------------------------------------
#Make a back up of the generated password
initial_password_backup = initial_password
#------------------------------------------------------------------------------------------------------------------
print(initial_password)

#Loop through the password back up
for i in range(len(initial_password_backup)):
    #Choose a random character from the password generated and extract its index
    index_initial_password = initial_password.index(random.choice(initial_password))
    #Get the actual character with the obtained index
    Sel_char_initial_password = initial_password[index_initial_password]
    #Add the character to the new password variable
    final_password += Sel_char_initial_password
    #Remove the character from the initial password variable, so it can't be chosen again.
    # Combine the part before the index and the part after the index
    initial_password = initial_password[:index_initial_password] + initial_password[index_initial_password + 1:]

print("Your password is: " + final_password)

# print(f"Initial password is: {initial_password_backup}")
# print(f"Initial password current content: {initial_password}")
# print(f"Final password is: {final_password}")

# print(initial_password)
# index_initial_password = initial_password.index(random.choice(initial_password))
# print(index_initial_password)
# Sel_char_initial_password = initial_password[index_initial_password]
# print(Sel_char_initial_password)
#     final_password = ""
#
# print(initial_password)
# print(len(initial_password))
# print(initial_password_backup)
# print(len(initial_password_backup))
# print(len(final_password))