import tkinter as tk


class AccountGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Create Account")
        self.window.geometry("400x350")

        title_label = tk.Label(
            self.window,
            text="Create Account",
            font=("Arial", 20)
        )
        title_label.pack(pady=20)

        instructions_label = tk.Label(
            self.window,
            text="Enter a username and password to create an account."
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

        print("Account created")
        print("Username:", username)
        print("Password:", password)

    def cancel(self):
        self.window.destroy()
