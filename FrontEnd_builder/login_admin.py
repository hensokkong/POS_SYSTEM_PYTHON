import subprocess
import sys
import tkinter as tk
from tkinter import messagebox


Password_IT ="IT1234"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "1234"

MAX_ATTEMPTS = 3
failed_attempts = 0
account_locked = False


def login():
    global failed_attempts, account_locked

    if account_locked:
        message_label.config(
            text="Account locked. Please contact IT.",
            fg="red"
        )
        return

    user = user_entry.get().strip()
    password = password_entry.get()

    if user == "":
        message_label.config(
            text="Please enter your username.",
            fg="red"
        )
        return

    if password == "":
        message_label.config(
            text="Please enter your password.",
            fg="red"
        )
        return

    if user == ADMIN_USER and password == ADMIN_PASSWORD:
        failed_attempts = 0

        message_label.config(
            text="Login successful!",
            fg="green"
        )

        subprocess.Popen([sys.executable, "Add_Product.py"])
        root.destroy()

    else:
        failed_attempts += 1

        remaining = MAX_ATTEMPTS - failed_attempts

        if failed_attempts >= MAX_ATTEMPTS:
            lock_account()

        else:
            message_label.config(
                text=f"Wrong username or password! {remaining} attempt(s) remaining.",
                fg="red"
            )


def lock_account():
    global account_locked

    account_locked = True

    user_entry.config(state="disabled")
    password_entry.config(state="disabled")
    login_button.config(state="disabled")

    message_label.config(
        text="Account locked. Please contact IT to unlock.",
        fg="red"
    )


def unlock_account():
    global failed_attempts, account_locked

    failed_attempts = 0
    account_locked = False

    user_entry.config(state="normal")
    password_entry.config(state="normal")
    login_button.config(state="normal")

    user_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    message_label.config(
        text="Account unlocked. You can login again.",
        fg="green"
    )

    user_entry.focus()


def open_admin():
    admin_window = tk.Toplevel(root)

    admin_window.title("Admin")
    admin_window.geometry("500x400")
    admin_window.resizable(False, False)
    admin_window.configure(bg="white")

    admin_title = tk.Label(
        admin_window,
        text="Admin Dashboard",
        font=("Arial", 24, "bold"),
        bg="white",
        fg="black"
    )

    admin_title.pack(pady=50)

    logout_button = tk.Button(
        admin_window,
        text="Logout",
        font=("Arial", 13, "bold"),
        bg="#D9534F",
        fg="white",
        activebackground="#c9302c",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=admin_window.destroy
    )

    logout_button.pack(
        ipadx=30,
        ipady=10
    )


def open_it_unlock():
    it_window = tk.Toplevel(root)

    it_window.title("IT Unlock")
    it_window.geometry("400x300")
    it_window.resizable(False, False)
    it_window.configure(bg="white")

    title = tk.Label(
        it_window,
        text="IT Account Unlock",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="black"
    )

    title.pack(pady=(35, 25))

    info = tk.Label(
        it_window,
        text="Enter IT password to unlock the account.",
        font=("Arial", 11),
        bg="white",
        fg="#555555"
    )

    info.pack(pady=(0, 15))

    it_password_entry = tk.Entry(
        it_window,
        font=("Arial", 14),
        bg="#e5e5e5",
        relief="flat",
        show="*"
    )

    it_password_entry.pack(
        fill="x",
        padx=50,
        ipady=8
    )

    it_message = tk.Label(
        it_window,
        text="",
        font=("Arial", 10),
        bg="white"
    )

    it_message.pack(pady=10)

    def check_it_password():
        it_password = it_password_entry.get()

        if it_password == Password_IT:
            unlock_account()
            it_window.destroy()
        else:
            it_message.config(
                text="Wrong IT password.",
                fg="red"
            )

    unlock_button = tk.Button(
        it_window,
        text="Unlock Account",
        font=("Arial", 12, "bold"),
        bg="#337AB7",
        fg="white",
        activebackground="#286090",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=check_it_password
    )

    unlock_button.pack(
        ipadx=20,
        ipady=8
    )

    it_password_entry.focus()


root = tk.Tk()

root.title("Login-Admin")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#f7f7f7")


page_title = tk.Label(
    root,
    text="Login-Admin",
    font=("Arial", 13),
    fg="#aaaaaa",
    bg="#f7f7f7"
)

page_title.place(
    x=15,
    y=10
)


card = tk.Frame(
    root,
    bg="white",
    highlightbackground="#eeeeee",
    highlightthickness=1
)

card.place(
    relx=0.5,
    rely=0.52,
    relwidth=0.88,
    relheight=0.88,
    anchor="center"
)


content = tk.Frame(
    card,
    bg="white"
)

content.place(
    relx=0.5,
    rely=0.5,
    relwidth=0.78,
    relheight=0.95,
    anchor="center"
)


title = tk.Label(
    content,
    text="Login",
    font=("Arial", 32),
    bg="white",
    fg="black"
)

title.pack(
    pady=(10, 25)
)


user_label = tk.Label(
    content,
    text="User",
    font=("Arial", 15),
    bg="white",
    fg="black",
    anchor="w"
)

user_label.pack(
    fill="x",
    padx=10
)


user_entry = tk.Entry(
    content,
    font=("Arial", 15),
    bg="#e5e5e5",
    relief="flat"
)

user_entry.pack(
    fill="x",
    ipady=8,
    pady=(5, 15)
)


password_label = tk.Label(
    content,
    text="Password",
    font=("Arial", 15),
    bg="white",
    fg="black",
    anchor="w"
)

password_label.pack(
    fill="x",
    padx=10
)


password_entry = tk.Entry(
    content,
    font=("Arial", 15),
    bg="#e5e5e5",
    relief="flat",
    show="*"
)

password_entry.pack(
    fill="x",
    ipady=8,
    pady=(5, 15)
)


login_button = tk.Button(
    content,
    text="Login",
    command=login,
    font=("Arial", 15),
    fg="white",
    bg="#58cf45",
    activebackground="#4bc239",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

login_button.pack(
    ipadx=40,
    ipady=8,
    pady=(0, 15)
)


message_label = tk.Label(
    content,
    text="",
    font=("Arial", 11),
    bg="white",
    fg="red"
)

message_label.pack(
    pady=5
)


it_button = tk.Button(
    content,
    text="IT Unlock",
    command=open_it_unlock,
    font=("Arial", 11, "underline"),
    fg="#337AB7",
    bg="white",
    activebackground="white",
    activeforeground="#286090",
    relief="flat",
    cursor="hand2"
)

it_button.pack(
    pady=10
)


root.bind(
    "<Return>",
    lambda event: login()
)

root.bind(
    "<Escape>",
    lambda event: root.destroy()
)


user_entry.focus()

root.mainloop()