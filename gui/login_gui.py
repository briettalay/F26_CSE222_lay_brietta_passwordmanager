import tkinter as tk
from tkinter import messagebox
import os

from application.password_manager import PasswordManagerGUI


class LoginGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Login")
        self.window.geometry("400x350")

        title_label = tk.Label(
            self.window,
            text="Login",
            font=("Arial", 20)
        )
        title_label.pack(pady=20)

        instructions_label = tk.Label(
            self.window,
            text="Enter your username and password to login."
        )
        instructions_label.pack(pady=10)

        username_label = tk.Label(
            self.window,
            text="Username:"
        )
        username_label.pack()

        self.username_entry = tk.Entry(
            self.window,
            width=30,
            justify="right"
        )
        self.username_entry.pack(pady=5)

        password_label = tk.Label(
            self.window,
            text="Password:"
        )
        password_label.pack()

        self.password_entry = tk.Entry(
            self.window,
            width=30,
            show="*",
            justify="right"
        )
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(
            self.window,
            text="Login",
            width=20,
            command=self.login
        )
        self.login_button.pack(pady=15)

        cancel_button = tk.Button(
            self.window,
            text="Cancel",
            width=20,
            command=self.cancel
        )
        cancel_button.pack()

        self.password_entry.bind(
            "<Return>",
            self.login
        )

    def login(self, event=None):
        self.login_button.config(state="disabled")

        username = self.username_entry.get()
        password = self.password_entry.get()

        account_file = "data/account.txt"

        if not os.path.exists(account_file):
            messagebox.showerror(
                "Login Error",
                "No account exists. Please create an account first."
            )

            self.login_button.config(state="normal")
            return

        with open(account_file, "r") as file:
            stored_username = file.readline().strip()
            stored_password = file.readline().strip()

        if username == stored_username and password == stored_password:
            self.window.destroy()
            PasswordManagerGUI()

        else:
            messagebox.showerror(
                "Login Error",
                "Invalid username or password."
            )

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            self.login_button.config(state="normal")

    def cancel(self):
        self.window.destroy()
