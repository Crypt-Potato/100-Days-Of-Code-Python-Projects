from tkinter import *
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# colors
LIGHT_BLUE = "#DEECEC"

# variables
encrypted_password = None

# functions
def encrypt_password():
    global encrypted_password, f

    password = master_password_entry.get()

    encrypted_password = f.encrypt(bytes(password, "utf-8"))

    with open("passwords.txt", mode="x") as file:
        file.write(str(encrypted_password))

window = Tk()
window.config(padx=50, pady=50, bg=LIGHT_BLUE)

canvas = Canvas(width=150, height=150, highlightthickness=0)
lock_img = PhotoImage(file="lock_image.png")
canvas.create_image(75, 75, image=lock_img)
canvas.pack()

master_password_entry = Entry()
master_password_entry.pack()

enter_button = Button(text="enter", command=encrypt_password)
enter_button.pack()

window.mainloop()
