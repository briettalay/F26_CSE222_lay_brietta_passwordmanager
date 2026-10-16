import tkinter as tk


class LoginGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Login")
        self.window.geometry("400x300")

        title_label = tk.Label(
            self.window,
            text="Login",
            font=("Arial", 20)
        )
        title_label.pack(pady=20)

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

        login_button = tk.Button(
            self.window,
            text="Login",
            width=20,
            command=self.login
        )
        login_button.pack(pady=15)

        cancel_button = tk.Button(
            self.window,
            text="Cancel",
            width=20,
            command=self.cancel
        )
        cancel_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        print("Login username:", username)
        print("Login password:", password)

    def cancel(self):
        self.window.destroy()
