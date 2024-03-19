import tkinter as tk
from tkinter import ttk
from ciphers.Vigenere_cipher import VigenereCipher
from ciphers.Simple_permutation_cipher import SimplePermutationCipher


class CipherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Приложение для шифрования")

        self.frame = ttk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text="Выберите тип шифра:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.cipher_type_menu = ttk.Combobox(self.frame, values=["Виженера", "Простой перестановки"])
        self.cipher_type_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.cipher_type_menu.set("Виженера")
        self.cipher_type_menu.bind("<<ComboboxSelected>>", self.toggle_key_entry)

        ttk.Label(self.frame, text="Выберите язык:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.language_menu = ttk.Combobox(self.frame, values=["английский", "русский"])
        self.language_menu.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.language_menu.set("английский")

        self.key_label = ttk.Label(self.frame, text="Введите ключ:")
        self.key_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.key_entry = ttk.Entry(self.frame)
        self.key_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.frame, text="Введите текст:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.text_entry = ttk.Entry(self.frame)
        self.text_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Button(self.frame, text="Зашифровать", command=self.encrypt_text).grid(row=4, column=0, padx=5, pady=5,
                                                                                   sticky="w")
        ttk.Button(self.frame, text="Расшифровать", command=self.create_decryption_window).grid(row=4, column=1, padx=5, pady=5,
                                                                                    sticky="w")

        ttk.Button(self.frame, text="Очистить", command=self.clear_text).grid(row=5, column=0, columnspan=2,
                                                                               padx=5, pady=5, sticky="w")

        ttk.Button(self.frame, text="Копировать зашифрованный текст", command=self.copy_encrypted_text).grid(row=6, column=0, columnspan=2,
                                                                              padx=5, pady=5, sticky="w")
        ttk.Button(self.frame, text="Копировать расшифрованный текст", command=self.copy_decrypted_text).grid(row=9,
                                                                                                             column=0,
                                                                                                             columnspan=2,
                                                                                                             padx=5,
                                                                                                             pady=5,
                                                                                                             sticky="w")

        self.encrypted_result_label = ttk.Label(self.frame, text="")
        self.encrypted_result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        self.decrypted_result_label = ttk.Label(self.frame, text="")
        self.decrypted_result_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    def toggle_key_entry(self, event):
        selected_cipher = self.cipher_type_menu.get()
        if selected_cipher == "Простой перестановки":
            self.key_label.grid_remove()
            self.key_entry.grid_remove()
        else:
            self.key_label.grid()
            self.key_entry.grid()

    def get_cipher(self):
        cipher_type = self.cipher_type_menu.get()
        language = self.language_menu.get()
        key = self.key_entry.get()
        text = self.text_entry.get()

        if cipher_type == "Виженера":
            if language == "английский":
                alphabet = 'english'
            else:
                alphabet = 'russian'
            return VigenereCipher(alphabet=alphabet), text, key if key else None
        elif cipher_type == "Простой перестановки":
            if language == "английский":
                alphabet = 'english'
            else:
                alphabet = 'russian'
            return SimplePermutationCipher(alphabet=alphabet), text

    def encrypt_text(self):
        cipher_type = self.cipher_type_menu.get()
        if cipher_type == "Виженера":
            cipher, text, key = self.get_cipher()
            result = cipher.encryption(text, key)
            self.encrypted_result_label.config(text=f"Зашифрованный текст: {result}")
        elif cipher_type == "Простой перестановки":
            cipher, text = self.get_cipher()
            result = cipher.encryption(text)
            self.encrypted_result_label.config(text=f"Зашифрованный текст: {result}")

    def create_decryption_window(self):
        decryption_window = tk.Toplevel(self.master)
        decryption_window.title("Расшифровка")

        ttk.Label(decryption_window, text="Введите текст:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        text_entry = ttk.Entry(decryption_window)
        text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Button(decryption_window, text="Расшифровать",
                   command=lambda: self.decrypt_text_in_window(decryption_window, text_entry)).grid(row=1, column=0,
                                                                                                    columnspan=2,
                                                                                                    padx=5, pady=5,
                                                                                                    sticky="w")

        ttk.Button(decryption_window, text="Вставить скопированный текст",
                   command=lambda: self.paste_text(text_entry)).grid(row=2, column=0, columnspan=2, padx=5, pady=5,
                                                                     sticky="w")

    def decrypt_text_in_window(self, window, text_entry):
        cipher_type = self.cipher_type_menu.get()
        encrypted_text = text_entry.get()
        if cipher_type == "Виженера":
            cipher, text, key = self.get_cipher()
            result = cipher.decryption(encrypted_text, key)
            self.decrypted_result_label.config(text=f"Расшифрованный текст: {result}")
        elif cipher_type == "Простой перестановки":
            cipher, text = self.get_cipher()
            result = cipher.decryption(encrypted_text)
            self.decrypted_result_label.config(text=f"Расшифрованный текст: {result}")
        window.destroy()

    def clear_text(self):
        self.text_entry.delete(0, tk.END)
        self.encrypted_result_label.config(text="")
        self.decrypted_result_label.config(text="")
        self.key_entry.delete(0, tk.END)

    def copy_encrypted_text(self):
        full_text = self.encrypted_result_label.cget("text")
        start_index = full_text.find("Зашифрованный текст:") + len("Зашифрованный текст:")
        encrypted_text = full_text[start_index:].strip()
        self.master.clipboard_clear()
        self.master.clipboard_append(encrypted_text)

    def copy_decrypted_text(self):
        full_text = self.decrypted_result_label.cget("text")
        start_index = full_text.find("Расшифрованный текст:") + len("Расшифрованный текст:")
        decrypted_text = full_text[start_index:].strip()
        self.master.clipboard_clear()
        self.master.clipboard_append(decrypted_text)

    def paste_text(self, text_entry):
        text_to_paste = self.master.clipboard_get()
        if text_to_paste:
            text_entry.delete(0, tk.END)
            text_entry.insert(0, text_to_paste)


if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
