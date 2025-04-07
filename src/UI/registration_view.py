"""This module includes functions to show the registration view and handle the operations
that can be done on the registration page"""

from tkinter import StringVar, Label
import tkinter as tk
from logic.dreamland_logic import dreamland_logic, UsernameTakenError, InvalidCredentialsError


class RegistrationView:
    """Class taking care of showing the registration page"""
    def __init__(self, root, handle_registration, handle_show_login_view):
        self._root = root
        self._handle_registration = handle_registration
        self._handle_show_login_view = handle_show_login_view
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def destroy(self):
        """Don't show the window"""
        self._frame.destroy()

    def _registration_handler(self):
        """Create the new user"""
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            dreamland_logic.create_new_user(username, password)
            self._handle_registration()
        except InvalidCredentialsError:
            if not 3 <= len(username) <= 20:
                self._error_message("Käyttäjänimen tulee olla 3-20 merkkiä")
            if len(password) < 5:
                self._error_message("Salasanan tulee olla vähintään 5 merkkiä")
        except UsernameTakenError:
            self._error_message("Tämä käyttäjänimi on jo käytössä")

    def _error_message(self, message):
        """Show error message"""
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Hide the error message"""
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """Field to write username"""
        tk.Label(master=self._frame, text="Käyttäjänimi:", font=("Bookman", 12),
                 fg="#00044A", bg="#D0F1FF").grid(row=1, column=0, sticky="w", pady=5)
        self._username_entry = tk.Entry(master=self._frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF")

        self._username_entry.grid(row=1, column=1, pady=5, sticky="w")

    def _initialize_password_field(self):
        """Field to write password"""
        tk.Label(master=self._frame, text="Salasana:", font=("Bookman", 12),
                 fg="#00044A", bg="#D0F1FF").grid(row=2, column=0, sticky="w", pady=5)
        self._password_entry = tk.Entry(master=self._frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF")

        self._password_entry.grid(row=2, column=1, pady=5, sticky="w")

    def _initialize(self):
        self._frame = tk.Frame(
            master=self._root, bg="#D0F1FF", padx=20, pady=20)
        self._frame.place(relx=0.7, rely=0.4, anchor="center")
        Label(self._frame, text="Rekisteröidy", font=("Bookman", 20, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self._error_variable = StringVar(self._frame)
        self._error_label = tk.Label(master=self._frame, textvariable=self._error_variable,
                                     font=("Bookman", 15, "bold"), bg="#D0F1FF", fg="#FC2D7D")
        self._error_label.grid(row=0, column=1, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        create_button = tk.Button(master=self._frame, text="Luo käyttäjä",
                                  font=("Bookman", 14, "bold"), bg="#FADCD9",
                                  fg="#00044A", padx=30, pady=8, borderwidth=0,
                                  command=self._registration_handler)
        create_button.grid(row=4, column=0, sticky="w", pady=10)

        login_button = tk.Button(master=self._frame, text="Takaisin kirjautumissivulle",
                                 font=("Bookman", 14, "bold"),
                                 bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                 command=self._handle_show_login_view)
        login_button.grid(row=6, column=0, sticky="w", pady=10)

        self._hide_error()
