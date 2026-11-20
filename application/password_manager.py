
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os


class PasswordManagerGUI:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Password Manager")
        self.window.geometry("600x500")

        self.display_window = None
        self.tree = None

        # Original layout
        tk.Label(
            self.window,
            text="Password Manager",
            font=("Arial", 18, "bold")
        ).pack(pady=15)

        tk.Label(
            self.window,
            text="Enter the information for your password entry below."
        ).pack(pady=5)

        form = tk.Frame(self.window)
        form.pack(pady=15)

        tk.Label(form, text="Description:").grid(
            row=0, column=0, padx=10, pady=10, sticky="e"
        )
        self.description_entry = tk.Entry(form, width=35)
        self.description_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form, text="Username:").grid(
            row=1, column=0, padx=10, pady=10, sticky="e"
        )
        self.username_entry = tk.Entry(form, width=35)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form, text="Password:").grid(
            row=2, column=0, padx=10, pady=10, sticky="e"
        )
        self.password_entry = tk.Entry(form, width=35)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=15)

        tk.Button(
            button_frame, text="Update",
            width=12, command=self.update
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            button_frame, text="Search",
            width=12, command=self.search
        ).grid(row=0, column=1, padx=8)

        tk.Button(
            button_frame, text="Display All",
            width=12, command=self.display_all
        ).grid(row=0, column=2, padx=8)

        tk.Button(
            self.window, text="Delete",
            width=12, command=self.delete
        ).pack(pady=8)

        tk.Button(
            self.window, text="Exit",
            width=12, command=self.cancel
        ).pack(pady=8)

    def get_password_file(self):
        os.makedirs("data", exist_ok=True)
        return os.path.join("data", "passwords.txt")

    def load_entries(self):
        filename = self.get_password_file()
        entries = []

        if not os.path.exists(filename):
            return entries

        with open(filename, "r") as file:
            lines = file.read().splitlines()

        for i in range(0, len(lines) - 2, 3):
            entries.append((
                lines[i],
                lines[i + 1],
                lines[i + 2]
            ))

        return entries

    def save_entries(self, entries):
        filename = self.get_password_file()

        with open(filename, "w") as file:
            for description, username, password in entries:
                file.write(description + "\n")
                file.write(username + "\n")
                file.write(password + "\n")

        # Automatically refresh the open Display All window.
        if self.display_window is not None:
            if self.display_window.winfo_exists():
                self.display_window.after_idle(
                    self.refresh_display_window
                )

    def update(self):
        description = self.description_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not description or not username or not password:
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        entries = self.load_entries()
        updated = False

        for i, entry in enumerate(entries):
            if entry[0].lower() == description.lower():
                entries[i] = (description, username, password)
                updated = True
                break

        if not updated:
            entries.append((description, username, password))

        self.save_entries(entries)

        messagebox.showinfo(
            "Success",
            "Password entry saved successfully."
        )

        self.clear_entries()

    def search(self):
        description = self.description_entry.get().strip()

        if not description:
            messagebox.showwarning(
                "Missing Information",
                "Please enter a description to search."
            )
            return

        entries = self.load_entries()

        for entry in entries:
            if entry[0].lower() == description.lower():
                self.username_entry.delete(0, tk.END)
                self.username_entry.insert(0, entry[1])

                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, entry[2])
                return

        messagebox.showinfo(
            "Not Found",
            "No password entry was found."
        )

    def display_all(self):
        if (
            self.display_window is not None
            and self.display_window.winfo_exists()
        ):
            self.display_window.lift()
            self.refresh_display_window()
            return

        self.display_window = tk.Toplevel(self.window)
        self.display_window.title("All Password Entries")
        self.display_window.geometry("650x350")

        columns = ("Description", "Username", "Password")

        self.tree = ttk.Treeview(
            self.display_window,
            columns=columns,
            show="headings"
        )

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=200)

        scrollbar = ttk.Scrollbar(
            self.display_window,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.display_window.protocol(
            "WM_DELETE_WINDOW",
            self.close_display_window
        )

        self.refresh_display_window()

    def refresh_display_window(self):
        if self.display_window is None:
            return

        if not self.display_window.winfo_exists():
            self.display_window = None
            self.tree = None
            return

        if self.tree is None or not self.tree.winfo_exists():
            return

        for item in self.tree.get_children():
            self.tree.delete(item)

        entries = self.load_entries()
        entries.sort(key=lambda entry: entry[0].casefold())

        for description, username, password in entries:
            self.tree.insert(
                "",
                tk.END,
                values=(description, username, password)
            )

    def close_display_window(self):
        if self.display_window is not None:
            self.display_window.destroy()

        self.display_window = None
        self.tree = None

    def delete(self):
        description = self.description_entry.get().strip()

        if not description:
            messagebox.showwarning(
                "Missing Information",
                "Please enter a description to delete."
            )
            return

        entries = self.load_entries()

        updated_entries = [
            entry for entry in entries
            if entry[0].lower() != description.lower()
        ]

        if len(updated_entries) == len(entries):
            messagebox.showinfo(
                "Not Found",
                "No password entry was found."
            )
            return

        self.save_entries(updated_entries)

        messagebox.showinfo(
            "Success",
            "Password entry deleted successfully."
        )

        self.clear_entries()

    def clear_entries(self):
        self.description_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def cancel(self):
        if self.display_window is not None:
            self.close_display_window()

        self.window.destroy()
