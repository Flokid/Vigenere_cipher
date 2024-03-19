import random
import re

class SimplePermutationCipher:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        if self.alphabet == 'english':
            self.alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif self.alphabet == 'russian':
            self.alphabet_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    def clean_text(self, text):
        cleaned_text = re.sub(r'[^A-Za-zА-Яа-яЁё]', '', text.upper())
        return cleaned_text

    def encryption(self, plaintext):
        plaintext = self.clean_text(plaintext)
        while len(plaintext) % 5 != 0:
            plaintext += random.choice(self.alphabet_uppercase)
        reversed_text = plaintext[::-1]
        groups = [reversed_text[i:i + 5] for i in range(0, len(reversed_text), 5)]
        encrypted_text = ' '.join(groups)
        return encrypted_text

    def decryption(self, ciphertext):
        decrypted_text = ciphertext[::-1]
        return decrypted_text

