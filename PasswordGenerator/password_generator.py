import string
from random import choice
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine Zahl eingeben.")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = '!"§$%&/()='

    all_chars = lower + upper + digits + special

    password = "".join(choice(all_chars) for _ in range(length))

    result_var.set(password)

    # Ausgabe zusätzlich in der Konsole
    print("Passwort:", password)

root = tk.Tk()
root.title("Passwort Generator")
root.geometry("400x150")

tk.Label(root, text="Passwortlänge:").pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root, text="Generieren", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=50).pack()

root.mainloop()