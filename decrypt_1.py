import string

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.alphabet = string.ascii_uppercase

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        encrypted_text = ''
        key_index = 0
        for char in plaintext:
            if char in self.alphabet:
                shift = self.alphabet.index(self.key[key_index % len(self.key)])
                encrypted_char = self.alphabet[(self.alphabet.index(char) + shift) % 26]
                encrypted_text += encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = ''
        key_index = 0
        for char in ciphertext:
            if char in self.alphabet:
                shift = self.alphabet.index(self.key[key_index % len(self.key)])
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
        return self.encrypt(ciphertext)  # Atbash Cipher is its own inverse

# Original Message
original_message = "THIS IS JUST AN EXAMPLE TO EXPLAIN THE PROBLEM"

# Encryption
vigenere_cipher = VigenereCipher("KEYWORD")
keyword_cipher = KeywordCipher("SECRET")
atbash_cipher = AtbashCipher()

encrypted_message_1 = vigenere_cipher.encrypt(original_message)
encrypted_message_2 = keyword_cipher.encrypt(encrypted_message_1)
encrypted_message_3 = atbash_cipher.encrypt(encrypted_message_2)

print("Original Message:", original_message)
print("Encrypted Message 1 (Vigenère Cipher):", encrypted_message_1)
print("Encrypted Message 2 (Keyword Cipher):", encrypted_message_2)
print("Encrypted Message 3 (Atbash Cipher):", encrypted_message_3)
print()

# Decryption (in reverse order)
decrypted_message_3 = atbash_cipher.decrypt(encrypted_message_3)
decrypted_message_2 = keyword_cipher.decrypt(decrypted_message_3)
decrypted_message_1 = vigenere_cipher.decrypt(decrypted_message_2)

print("Decrypted Message 1 (Vigenère Cipher):", decrypted_message_1)
print("Decrypted Message 2 (Keyword Cipher):", decrypted_message_2)
print("Decrypted Message 3 (Atbash Cipher):", decrypted_message_3)
