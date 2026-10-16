import tkinter as tk
from tkinter import messagebox


class AccountGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Create Account")
        self.window.geometry("450x350")

        title_label = tk.Label(
            self.window,
            text="Create Account",
            font=("Arial", 20)
        )
        title_label.pack(pady=20)

        instructions_label = tk.Label(
            self.window,
            text="Create a username and password for your account."
        )
        instructions_label.pack(pady=5)

        requirements_label = tk.Label(
            self.window,
            text="Password must be at least 9 characters,\n"
                 "with an uppercase letter, lowercase letter, and digit."
        )
        requirements_label.pack(pady=5)

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

        self.username_entry.focus_set()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Username and password are required."
            )
            return

        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        if len(password) < 9:
            messagebox.showerror(
                "Error",
                "Password must be at least 9 characters."
            )
            return

        if not any(character.isupper() for character in password):
            messagebox.showerror(
                "Error",
                "Password must contain an uppercase letter."
            )
            return

        if not any(character.islower() for character in password):
            messagebox.showerror(
                "Error",
                "Password must contain a lowercase letter."
            )
            return

        if not any(character.isdigit() for character in password):
            messagebox.showerror(
                "Error",
                "Password must contain a digit."
            )
            return

        messagebox.showinfo(
            "Success",
            "Account created successfully!"
        )

    def cancel(self):
        self.window.destroy()
