import os
import tkinter as tk
from PIL import Image, ImageTk


def is_russian(text):
    russian_letters = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                       'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
    text_lower = text.lower()
    russian_count = sum(1 for char in text_lower if char in russian_letters)
    return russian_count / len(text_lower) > 0.1


def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
            print(key)
    return "".join(key)


def create_vigenere_table(alphabet):
    table = []
    for i in range(len(alphabet)):
        row = alphabet[i:] + alphabet[:i]
        table.append(row)
    return table


def encryption(text, key, alphabet):
    table = create_vigenere_table(alphabet)

    encrypted_text = ''
    key_index = 0

    for char in text:
        if char.lower() in alphabet:
            char_index = alphabet.index(char.lower())
            row_index = alphabet.index(key[key_index].lower())
            new_char = table[row_index][char_index]
            encrypted_text += new_char.upper() if char.isupper() else new_char
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char

    return encrypted_text


def decryption(encrypted_text, key, alphabet):
    table = create_vigenere_table(alphabet)

    decrypted_text = ''
    key_index = 0

    for char in encrypted_text:
        if char.lower() in alphabet:
            char_index = table[alphabet.index(key[key_index].lower())].index(char.lower())
            new_char = alphabet[char_index]
            decrypted_text += new_char.upper() if char.isupper() else new_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char

    return decrypted_text


def on_encrypt():
    string = entry_string.get()
    keyword = entry_keyword.get().replace(" ", "")
    key = generate_key(string, keyword)
    if is_russian(string):
        russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        encrypt_text = encryption(string, key, russian_alphabet)
        result_label.config(
            text=f"Encrypted message: {encrypt_text}\nKeyword: {keyword}\nDecrypted message: {decryption(encrypt_text, key, russian_alphabet)}")
    else:
        english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        encrypt_text = encryption(string, key, english_alphabet)
        result_label.config(
            text=f"Encrypted message: {encrypt_text}\nKeyword: {keyword}\nDecrypted message: {decryption(encrypt_text, key, english_alphabet)}")


gui = tk.Tk()
gui.title("Vigenere Encryption")
gui.geometry("1920x1080")
bg_image_path = os.path.join("bg/piggy.jpg")

image = Image.open(bg_image_path)
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(gui, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_string = tk.Label(gui, text="Enter the message:")
label_string.pack()
entry_string = tk.Entry(gui)
entry_string.pack()

label_keyword = tk.Label(gui, text="Enter the keyword:")
label_keyword.pack()
entry_keyword = tk.Entry(gui)
entry_keyword.pack()

button_encrypt = tk.Button(gui, text="Encrypt/Decrypt", command=on_encrypt)
button_encrypt.pack()

result_label = tk.Label(gui, text="")
result_label.pack()

if __name__ == "__main__":
    gui.mainloop()
