alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

initial_index = 0
final_index = 0
encoded_text = ""

def encrypt(original_text, shift_amount):

    global initial_index
    global final_index
    global encoded_text

    for i in range(len(original_text)):
        initial_index = alphabet.index(original_text[i])
        final_index = initial_index
        for j in range(shift_amount):
            if final_index == len(alphabet)-1:
                final_index = -1
            final_index += 1
        encoded_text += alphabet[final_index]
    print(f"Here is the encoded result: {encoded_text}")


def decrypt(original_text, shift_amount):

    global initial_index
    global final_index
    global encoded_text

    for i in range(len(original_text)):
        initial_index = alphabet.index(original_text[i])
        final_index = initial_index
        for j in range((shift_amount - 1), -1, -1):
            if final_index == 0:
                final_index = len(alphabet)
            final_index -= 1
        encoded_text += alphabet[final_index]
    print(f"Here is the encoded result: {encoded_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)

# mjqqt

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# def encrypt(original_text, shift_amount):
# # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#     for i in original_text:
#         shifted_position = alphabet.index(i) + shift_amount

#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

