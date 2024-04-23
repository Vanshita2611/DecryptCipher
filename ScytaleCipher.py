# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:05:37 2024

@author: Prateek
"""

import math


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



"""

# Example usage:

plaintext = "HELLO WORLD"

key = "WORLD"
scytale_cipher = ScytaleCipher(len(key))  # Example diameter
encrypted_message = scytale_cipher.encrypt(plaintext)
print("Encrypted Message:", encrypted_message)

decrypted_message = scytale_cipher.decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message)


"""
