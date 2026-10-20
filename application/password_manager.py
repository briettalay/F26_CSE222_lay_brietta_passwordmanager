import tkinter as tk
from tkinter import messagebox
import os


class PasswordManagerGUI:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Password Manager")
        self.window.geometry("600x500")

        title_label = tk.Label(
            self.window,
            text="Password Manager",
            font=("Arial", 22)
        )
        title_label.pack(pady=20)

        instructions_label = tk.Label(
            self.window,
            text="Enter the information for a password entry."
        )
        instructions_label.pack(pady=5)

        description_frame = tk.Frame(self.window)
        description_frame.pack(pady=10)

        description_label = tk.Label(
            description_frame,
            text="Description:",
            width=15
        )
        description_label.pack(side=tk.LEFT)

        self.description_entry = tk.Entry(
            description_frame,
            width=35
        )
        self.description_entry.pack(side=tk.LEFT)

        username_frame = tk.Frame(self.window)
        username_frame.pack(pady=10)

        username_label = tk.Label(
            username_frame,
            text="Username:",
            width=15
        )
        username_label.pack(side=tk.LEFT)

        self.username_entry = tk.Entry(
            username_frame,
            width=35
        )
        self.username_entry.pack(side=tk.LEFT)

        password_frame = tk.Frame(self.window)
        password_frame.pack(pady=10)

        password_label = tk.Label(
            password_frame,
            text="Password:",
            width=15
        )
        password_label.pack(side=tk.LEFT)

        self.password_entry = tk.Entry(
            password_frame,
            width=35,
            show="*"
        )
        self.password_entry.pack(side=tk.LEFT)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=25)

        self.update_button = tk.Button(
            button_frame,
            text="Update",
            width=15,
            command=self.update
        )
        self.update_button.grid(row=0, column=0, padx=5)

        self.search_button = tk.Button(
            button_frame,
            text="Search",
            width=15,
            command=self.search
        )
        self.search_button.grid(row=0, column=1, padx=5)

        self.display_button = tk.Button(
            button_frame,
            text="Display All",
            width=15,
            command=self.display_all
        )
        self.display_button.grid(row=0, column=2, padx=5)

        self.delete_button = tk.Button(
            button_frame,
            text="Delete",
            width=15,
            command=self.delete
        )
        self.delete_button.grid(row=1, column=1, pady=10)

        exit_button = tk.Button(
            self.window,
            text="Exit",
            width=15,
            command=self.cancel
        )
        exit_button.pack(pady=10)

        self.update_button.config(state="disabled")
        self.search_button.config(state="disabled")
        self.delete_button.config(state="disabled")

        self.description_entry.bind(
            "<KeyRelease>",
            self.check_description
        )

    def check_description(self, event=None):
        description = self.description_entry.get().strip()

        if description:
            self.update_button.config(state="normal")
            self.search_button.config(state="normal")
            self.delete_button.config(state="normal")
        else:
            self.update_button.config(state="disabled")
            self.search_button.config(state="disabled")
            self.delete_button.config(state="disabled")

    def update(self):
        description = self.description_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if description == "":
            messagebox.showerror(
                "Error",
                "Description cannot be empty."
            )
            return

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Username and password cannot be empty."
            )
            return

        if not os.path.exists("data"):
            os.makedirs("data")

        password_file = "data/passwords.txt"

        if not os.path.exists(password_file):
            with open(password_file, "a") as file:
                file.write(description + "\n")
                file.write(username + "\n")
                file.write(password + "\n")

            messagebox.showinfo(
                "Success",
                "Password entry saved."
            )

            self.clear_entries()
            return

        with open(password_file, "r") as file:
            lines = file.readlines()

        found = False

        for i in range(0, len(lines), 3):
            if lines[i].strip() == description:
                lines[i + 1] = username + "\n"
                lines[i + 2] = password + "\n"
                found = True
                break

        if found:
            with open(password_file, "w") as file:
                file.writelines(lines)

            messagebox.showinfo(
                "Success",
                "Password entry updated."
            )
        else:
            with open(password_file, "a") as file:
                file.write(description + "\n")
                file.write(username + "\n")
                file.write(password + "\n")

            messagebox.showinfo(
                "Success",
                "Password entry saved."
            )

        self.clear_entries()

    def search(self):
        description = self.description_entry.get().strip()

        if not os.path.exists("data/passwords.txt"):
            messagebox.showinfo(
                "Search",
                "No password entries found."
            )
            return

        with open("data/passwords.txt", "r") as file:
            lines = file.readlines()

        found = False

        for i in range(0, len(lines), 3):
            saved_description = lines[i].strip()

            if saved_description == description:
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)

                self.username_entry.insert(
                    0,
                    lines[i + 1].strip()
                )

                self.password_entry.insert(
                    0,
                    lines[i + 2].strip()
                )

                found = True
                break

        if not found:
            messagebox.showinfo(
                "Search",
                "Password entry not found."
            )

    def display_all(self):
        password_file = "data/passwords.txt"

        if not os.path.exists(password_file):
            messagebox.showinfo(
                "Display All",
                "No password entries found."
            )
            return

        with open(password_file, "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            messagebox.showinfo(
                "Display All",
                "No password entries found."
            )
            return

        entries = []

        for i in range(0, len(lines), 3):
            description = lines[i].strip()
            username = lines[i + 1].strip()
            password = lines[i + 2].strip()

            entries.append(
                (description, username, password)
            )

        entries.sort()

        display_text = ""

        for entry in entries:
            display_text += "Description: " + entry[0] + "\n"
            display_text += "Username: " + entry[1] + "\n"
            display_text += "Password: " + entry[2] + "\n"
            display_text += "\n"

        messagebox.showinfo(
            "All Passwords",
            display_text
        )

    def delete(self):
        description = self.description_entry.get().strip()

        if not os.path.exists("data/passwords.txt"):
            messagebox.showinfo(
                "Delete",
                "No password entries found."
            )
            return

        with open("data/passwords.txt", "r") as file:
            lines = file.readlines()

        new_lines = []
        found = False

        for i in range(0, len(lines), 3):
            saved_description = lines[i].strip()

            if saved_description == description:
                found = True
            else:
                new_lines.append(lines[i])
                new_lines.append(lines[i + 1])
                new_lines.append(lines[i + 2])

        if found:
            with open("data/passwords.txt", "w") as file:
                file.writelines(new_lines)

            messagebox.showinfo(
                "Delete",
                "Password entry deleted."
            )

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

        else:
            messagebox.showinfo(
                "Delete",
                "Password entry not found."
            )

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.check_description()

    def cancel(self):
        self.window.destroy()
