
class VigenereCipher:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        if self.alphabet == 'english':
            self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        elif self.alphabet == 'russian':
            self.alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def generate_key(self, string_for_key, key):
        key = list(key)
        if len(string_for_key) == len(key):
            return key
        else:
            for i in range(len(string_for_key) - len(key)):
                key.append(key[i % len(key)])
            return "".join(key)

    def create_vigenere_table(self):
        table = []
        for i in range(len(self.alphabet)):
            row = self.alphabet[i:] + self.alphabet[:i]
            table.append(row)
        return table

    def encryption(self, text, key):
        table = self.create_vigenere_table()

        encrypted_text = ''
        key_index = 0

        for char in text:
            if char.lower() in self.alphabet:
                char_index = self.alphabet.index(char.lower())
                row_index = self.alphabet.index(key[key_index].lower())
                new_char = table[row_index][char_index]
                encrypted_text += new_char.upper() if char.isupper() else new_char
                key_index = (key_index + 1) % len(key)
            else:
                encrypted_text += char

        return encrypted_text


    def decryption(self, encrypted_text, key):
        table = self.create_vigenere_table()

        decrypted_text = ''
        key_index = 0

        for char in encrypted_text:
            if char.lower() in self.alphabet:
                char_index = table[self.alphabet.index(key[key_index].lower())].index(char.lower())
                new_char = self.alphabet[char_index]
                decrypted_text += new_char.upper() if char.isupper() else new_char
                key_index = (key_index + 1) % len(key)
            else:
                decrypted_text += char

        return decrypted_text
