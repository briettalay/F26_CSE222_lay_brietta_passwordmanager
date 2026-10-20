import tkinter as tk
from tkinter import messagebox
import os


class AccountGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Create Account")
        self.window.geometry("450x400")

        title_label = tk.Label(
            self.window,
            text="Create Account",
            font=("Arial", 20)
        )
        title_label.pack(pady=20)

        instructions_label = tk.Label(
            self.window,
            text="Create a username and password for your account.\n\n"
                 "Password must be at least 9 characters,\n"
                 "with an uppercase letter, lowercase letter, and digit."
        )
        instructions_label.pack(pady=10)

        username_label = tk.Label(
            self.window,
            text="Username:"
        )
        username_label.pack()

        self.username_entry = tk.Entry(
            self.window,
            width=30
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
            show="*"
        )
        self.password_entry.pack(pady=5)

        confirm_label = tk.Label(
            self.window,
            text="Confirm Password:"
        )
        confirm_label.pack()

        self.confirm_entry = tk.Entry(
            self.window,
            width=30,
            show="*"
        )
        self.confirm_entry.pack(pady=5)

        create_button = tk.Button(
            self.window,
            text="Create Account",
            width=20,
            command=self.create_account
        )
        create_button.pack(pady=15)

        cancel_button = tk.Button(
            self.window,
            text="Cancel",
            width=20,
            command=self.cancel
        )
        cancel_button.pack()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        if username == "":
            messagebox.showerror(
                "Error",
                "Username cannot be empty."
            )
            return

        if password == "":
            messagebox.showerror(
                "Error",
                "Password cannot be empty."
            )
            return

        if len(password) < 9:
            messagebox.showerror(
                "Error",
                "Password must be at least 9 characters."
            )
            return

        if not any(char.isupper() for char in password):
            messagebox.showerror(
                "Error",
                "Password must contain an uppercase letter."
            )
            return

        if not any(char.islower() for char in password):
            messagebox.showerror(
                "Error",
                "Password must contain a lowercase letter."
            )
            return

        if not any(char.isdigit() for char in password):
            messagebox.showerror(
                "Error",
                "Password must contain a digit."
            )
            return

        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        account_file = "data/account.txt"

        os.makedirs("data", exist_ok=True)

        if os.path.exists(account_file):
            with open(account_file, "r") as file:
                existing_username = file.readline().strip()

            if existing_username == username:
                messagebox.showerror(
                    "Error",
                    "That username already exists."
                )
                return

        with open(account_file, "w") as file:
            file.write(username + "\n")
            file.write(password + "\n")

        messagebox.showinfo(
            "Account Created",
            "Account created successfully!"
        )

        self.window.destroy()

    def cancel(self):
        self.window.destroy()
