"""This module includes functions to show the registration view and handle the operations
that can be done on the registration page"""

from tkinter import StringVar, Label
import tkinter as tk
from ui.forms import FormHandler
from logic.dreamland_logic import dreamland_logic, UsernameTakenError, InvalidCredentialsError


class RegistrationView():
    """Class taking care of showing the registration page
    
    Attributes:
        root: TKinter element inside of which the view will be initialized
        handle_registration: value that is called when registering a new user
        handle_show_login_view: value that is called when moving to the login page
    """

    def __init__(self, root, handle_registration, handle_show_login_view):
        """Class taking care of showing the registration page
    
        Args:
            root: TKinter element inside of which the view will be initialized
            handle_registration: value that is called when registering a new user
            handle_show_login_view: value that is called when moving to the login page
        """

        self._root = root
        self._handle_registration = handle_registration
        self._handle_show_login_view = handle_show_login_view
        self.form_handler = FormHandler()

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self.form_handler.show_frame()

    def destroy(self):
        """Don't show the window"""
        self.form_handler.frame.destroy()

    def _registration_handler(self):
        """Creates the new user when registration is done"""
        username = self.form_handler.username_entry.get()
        password = self.form_handler.password_entry.get()

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
        """Shows the given error message on the page
        
        Args:
            message: string that describes the error message to be shown on the page
        """

        self.form_handler.error_variable.set(message)
        self.form_handler.error_label.grid()

    def _hide_error(self):
        """Hides the error message from the page"""
        self.form_handler.error_label.grid_remove()

    def _initialize_username_field(self):
        """Initializes the field where the user can write their username to register"""
        tk.Label(master=self.form_handler.frame, text="Käyttäjänimi:", font=("Bookman", 12),
                 fg="#00044A", bg="#D0F1FF").grid(row=1, column=0, sticky="w", pady=5)
        self.form_handler.username_entry = tk.Entry(master=self.form_handler.frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF")

        self.form_handler.username_entry.grid(row=1, column=1, pady=5, sticky="w")

    def _initialize_password_field(self):
        """Initializes the field where the user can write their password to register"""
        tk.Label(master=self.form_handler.frame, text="Salasana:", font=("Bookman", 12),
                 fg="#00044A", bg="#D0F1FF").grid(row=2, column=0, sticky="w", pady=5)
        self.form_handler.password_entry = tk.Entry(master=self.form_handler.frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF")

        self.form_handler.password_entry.grid(row=2, column=1, pady=5, sticky="w")

    def _initialize(self):
        """Initializes the registration page's ui"""
        self.form_handler.frame = tk.Frame(
            master=self._root, bg="#D0F1FF", padx=20, pady=20)
        self.form_handler.frame.place(relx=0.7, rely=0.4, anchor="center")
        Label(self.form_handler.frame, text="Rekisteröidy", font=("Bookman", 20, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.form_handler.error_variable = StringVar(self.form_handler.frame)
        self.form_handler.error_label = tk.Label(master=self.form_handler.frame,
                                                 textvariable=self.form_handler.error_variable,
                                                 font=("Bookman", 15, "bold"),
                                                 bg="#D0F1FF", fg="#FC2D7D")
        self.form_handler.error_label.grid(row=0, column=1, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        create_button = tk.Button(master=self.form_handler.frame, text="Luo käyttäjä",
                                  font=("Bookman", 14, "bold"), bg="#FADCD9",
                                  fg="#00044A", padx=30, pady=8, borderwidth=0,
                                  command=self._registration_handler)
        create_button.grid(row=4, column=0, sticky="w", pady=10)

        login_button = tk.Button(master=self.form_handler.frame, text="Takaisin kirjautumissivulle",
                                 font=("Bookman", 14, "bold"),
                                 bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                 command=self._handle_show_login_view)
        login_button.grid(row=6, column=0, sticky="w", pady=10)

        self._hide_error()
