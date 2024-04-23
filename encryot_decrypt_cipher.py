def vigenere_encrypt(plaintext, key):
    key = key.upper()
    encrypted_text = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def generate_keyword_alphabet(keyword):
    keyword = keyword.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword_alphabet = ""
    for char in keyword:
        if char not in keyword_alphabet:
            keyword_alphabet += char
    for char in alphabet:
        if char not in keyword_alphabet:
            keyword_alphabet += char
    return keyword_alphabet

def keyword_encrypt(plaintext, keyword):
    keyword_alphabet = generate_keyword_alphabet(keyword)
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += keyword_alphabet[ord(char) - ord('a')].lower()
            else:
                encrypted_text += keyword_alphabet[ord(char) - ord('A')]
        else:
            encrypted_text += char
    return encrypted_text

def atbash_encrypt(plaintext):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(ord('z') - (ord(char) - ord('a')))
            else:
                encrypted_text += chr(ord('Z') - (ord(char) - ord('A')))
        else:
            encrypted_text += char
    return encrypted_text

# Original Message
original_message = "This is just an example to explain the problem"

# Encryption
vigenere_key = "This"
partial_encryption_1 = vigenere_encrypt(original_message, vigenere_key)

keyword_key = "to"
partial_encryption_2 = keyword_encrypt(partial_encryption_1, keyword_key)

full_encryption = atbash_encrypt(partial_encryption_2)

print("Original Message:", original_message)
print("Full Final Encryption:", full_encryption)
