
import customtkinter as ctk
from tkinter import messagebox
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import customtkinter as ctk

# Configure appearance
ctk.set_appearance_mode("System")      # "Light", "Dark", or "System"
ctk.set_default_color_theme("blue")

# Create main window
app = ctk.CTk()
app.title("Hospital Management System")
app.geometry("500x400")
app.resizable(False, False)

# Title
title = ctk.CTkLabel(
    app,
    text="Hospital Management System",
    font=("Arial", 24, "bold")
)
title.pack(pady=30)

# Username
username_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Username"
)
username_entry.pack(pady=10)

# Password
password_entry = ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Password",
    show="*"
)
password_entry.pack(pady=10)

def login_user():

    username = username_entry.get()
    password = password_entry.get()

    user = login(username, password)

    if user:
        messagebox.showinfo("Success", f"Welcome {user[1]}!")

        app.destroy()

        # Later we will open the dashboard here.

    else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password."
        )

# Login button
login_button = ctk.CTkButton(
    app,
    text="Login",
    command=login_user
)
login_button.pack(pady=25)

app.mainloop()
