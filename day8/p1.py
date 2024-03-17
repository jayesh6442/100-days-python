letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key = int(input("Enter the key: "))
text = input("Enter the message: ")

# def encrypt_decrypt(key, text):
#     encrypted_text = ""
#     for letter in text:
#         if letter in letters:
#             position = letters.index(letter)
#             new_position = (position + key) % 26  # Using modulo to wrap around the alphabet
#             new_letter = letters[new_position]
#             encrypted_text += new_letter
#         else:
#             encrypted_text += letter  # Add non-alphabetic characters directly
#     print("Encrypted/Decrypted message:", encrypted_text)

# encrypt_decrypt(key, text)
def decrypt(encrypted_text,key):
    pain_text = ""
    for letter in encrypted_text:
        position = letters.index(letter)
        new_position = position - key
        new_letter = letters[new_position]
        pain_text+=new_letter
    print(pain_text)
    
decrypt(text,key)