import tkinter as tk
from .account_gui import AccountGUI
from .login_gui import LoginGUI


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Manager")
        self.window.geometry("400x300")

        title_label = tk.Label(
            self.window,
            text="Password Manager",
            font=("Arial", 20)
        )
        title_label.pack(pady=30)

        create_account_button = tk.Button(
            self.window,
            text="Create Account",
            width=20,
            command=self.create_account
        )
        create_account_button.pack(pady=10)

        login_button = tk.Button(
            self.window,
            text="Login",
            width=20,
            command=self.login
        )
        login_button.pack(pady=10)

        cancel_button = tk.Button(
            self.window,
            text="Cancel",
            width=20,
            command=self.cancel
        )
        cancel_button.pack(pady=10)

    def create_account(self):
        AccountGUI()

    def login(self):
        LoginGUI()

    def cancel(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()
