import string
import math
import random

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = string.ascii_uppercase

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted_text = ''
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                encrypted_char = self.alphabet[(self.alphabet.index(char) + shift) % 26]
                encrypted_text += encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        decrypted_text = ''
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                decrypted_char = self.alphabet[(self.alphabet.index(char) - shift) % 26]
                decrypted_text += decrypted_char
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text

class KeywordCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()
        self.alphabet = string.ascii_uppercase

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted_text = ''
        keyword_without_duplicates = ''.join(dict.fromkeys(self.keyword))

        modified_alphabet = keyword_without_duplicates
        for char in self.alphabet:
            if char not in keyword_without_duplicates:
                modified_alphabet += char

        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_text += modified_alphabet[index]
            else:
                encrypted_text += char

        return encrypted_text

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        decrypted_text = ''
        keyword_without_duplicates = ''.join(dict.fromkeys(self.keyword))

        modified_alphabet = keyword_without_duplicates
        for char in self.alphabet:
            if char not in keyword_without_duplicates:
                modified_alphabet += char

        for char in ciphertext:
            if char in self.alphabet:
                index = modified_alphabet.index(char)
                decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char

        return decrypted_text

class AtbashCipher:
    def __init__(self):
        self.alphabet = string.ascii_uppercase

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted_text = ''
        for char in plaintext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_char = self.alphabet[(len(self.alphabet) - 1) - index]
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)  # Atbash is its own inverse

class ScytaleCipher:
    def __init__(self, diameter):
        self.diameter = diameter

    def encrypt(self, plaintext):
        num_rows = math.ceil(len(plaintext) / self.diameter)
        padded_plaintext = plaintext.ljust(num_rows * self.diameter)

        encrypted_text = ''
        for col in range(self.diameter):
            for row in range(num_rows):
                index = col + row * self.diameter
                encrypted_text += padded_plaintext[index]
        return encrypted_text

    def decrypt(self, ciphertext):
        num_rows = math.ceil(len(ciphertext) / self.diameter)
        decrypted_text = ''
        for row in range(num_rows):
            for col in range(self.diameter):
                index = col * num_rows + row
                decrypted_text += ciphertext[index]
        return decrypted_text.strip()

class SubstitutionCipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = self.generate_random_key()

    def generate_random_key(self):
        alphabet = list(string.ascii_uppercase)
        random.shuffle(alphabet)
        return ''.join(alphabet)

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext.upper():
            if char.isalpha():
                index = ord(char) - ord('A')
                ciphertext += self.key[index]
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext.upper():
            if char.isalpha():
                index = self.key.index(char)
                plaintext += chr(index + ord('A'))
            else:
                plaintext += char
        return plaintext

# Define the decryption function
def decrypt_message(encrypted_message, algorithms):
    decrypted_message = encrypted_message
    for algorithm in reversed(algorithms):
        decrypted_message = algorithm.decrypt(decrypted_message)
    return decrypted_message

# Define the original message
original_message = "This is a test message to check decryption functionality."

# Encrypt the original message using the given algorithms
algorithms = [ScytaleCipher(3), AtbashCipher(), KeywordCipher("to")]
encrypted_message = original_message
for algorithm in algorithms:
    encrypted_message = algorithm.encrypt(encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt_message(encrypted_message, algorithms)

# Check if the decrypted message matches the original one
if decrypted_message == original_message:
    print("Decryption successful!")
    print("Original Message:", original_message)
    print("Decrypted Message:", decrypted_message)
else:
    print("Decryption failed!")
    print("Encrypted Message:", encrypted_message)
