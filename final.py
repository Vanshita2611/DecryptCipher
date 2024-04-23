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
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)]) - ord('A')
                if char.isupper():
                    encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
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
                if char.isupper():
                    decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
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

        # Create the modified alphabet by removing letters already in the keyword
        modified_alphabet = keyword_without_duplicates
        for char in self.alphabet:
            if char not in keyword_without_duplicates:
                modified_alphabet += char

        # Encrypt the plaintext using the modified alphabet
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

        # Create the modified alphabet by removing letters already in the keyword
        modified_alphabet = keyword_without_duplicates
        for char in self.alphabet:
            if char not in keyword_without_duplicates:
                modified_alphabet += char

        # Decrypt the ciphertext using the modified alphabet
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
        ciphertext = ciphertext.upper()
        decrypted_text = ''
        for char in ciphertext:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                decrypted_char = self.alphabet[(len(self.alphabet) - 1) - index]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text

# Define the message to be encrypted
original_message = "Python is a versatile programming language used for web development, data analysis, artificial intelligence, and more."

# Encrypt the message using the Vigenère cipher
vigenere_key = "KEYWORD"  # Example key
vigenere_cipher = VigenereCipher(vigenere_key)
encrypted_message_vigenere = vigenere_cipher.encrypt(original_message)

# Encrypt the message using the Keyword cipher
keyword = "PYTHON"  # Example keyword
keyword_cipher = KeywordCipher(keyword)
encrypted_message_keyword = keyword_cipher.encrypt(original_message)

# Encrypt the message using the Atbash cipher
atbash_cipher = AtbashCipher()
encrypted_message_atbash = atbash_cipher.encrypt(original_message)

print("Original Message:", original_message)
print("Encrypted Message (Vigenère):", encrypted_message_vigenere)
print("Encrypted Message (Keyword):", encrypted_message_keyword)
print("Encrypted Message (Atbash):", encrypted_message_atbash)

# Decrypt the encrypted message using the Atbash cipher
decrypted_message_atbash = atbash_cipher.decrypt(encrypted_message_atbash)

# Decrypt the encrypted message using the Keyword cipher
decrypted_message_keyword = keyword_cipher.decrypt(encrypted_message_keyword)

# Decrypt the encrypted message using the Vigenère cipher
decrypted_message_vigenere = vigenere_cipher.decrypt(encrypted_message_vigenere)

# Verify that the decrypted messages match the original message
print("Decrypted Message (Vigenère):", decrypted_message_vigenere)
