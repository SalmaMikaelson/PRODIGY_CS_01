import string 

# Define the lowercase alphabet for reference
alphabet = string.ascii_lowercase

# Function to encrypt a message using Caesar Cipher
def encrypt(text, shift_val):
    encrypted_text = ""
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift_val) % 26  # Shift the letter
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += letter  # Non-alphabet characters remain unchanged
    return encrypted_text

# Function to decrypt a message using Caesar Cipher
def decrypt(text, shift_val):
    decrypted_text = ""
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift_val) % 26  # Reverse shift
            decrypted_text += alphabet[new_index]
        else:
            decrypted_text += letter
    return decrypted_text

# Input from user for message and shift value
user_message = input("Enter a message: ").lower()  # Make sure to work with lowercase
shift_value = int(input("Enter the shift value: "))

# Encrypt and print the message
encrypted_result = encrypt(user_message, shift_value)
print("Encrypted message:", encrypted_result)

# Decrypt and print the message
decrypted_result = decrypt(encrypted_result, shift_value)
print("Decrypted message:", decrypted_result)
