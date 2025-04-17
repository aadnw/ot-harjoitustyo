"""This module includes functions to show the login view and handle the operations
that can be done on the login page"""

from tkinter import StringVar, Label
import tkinter as tk
from ui.forms import FormHandler
from logic.dreamland_logic import dreamland_logic, InvalidCredentialsError


class LoginView():
    """Class taking care of showing the login page"""

    def __init__(self, root, handle_login, handle_show_registration_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_registration_view = handle_show_registration_view
        self.form_handler = FormHandler()

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self.form_handler.show_frame()

    def destroy(self):
        """Don't show the window"""
        self.form_handler.frame.destroy()

    def _login_handler(self):
        """Login the user"""
        username = self.form_handler.username_entry.get()
        password = self.form_handler.password_entry.get()

        if username == '' or password == '':
            self._error_message("Käyttäjätunnus ja/tai salasana puuttuu")

        try:
            dreamland_logic.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._error_message("Virheellinen käyttäjänimi tai salasana")

    def _error_message(self, message):
        """Show error message"""
        self.form_handler.error_variable.set(message)
        self.form_handler.error_label.grid()

    def _initialize_username_field(self):
        """Field to write username"""
        tk.Label(self.form_handler.frame, text="Käyttäjänimi", font=("Bookman", 12), fg="#00044A",
                 bg="#D0F1FF").grid(row=1, column=0, columnspan=2, sticky="w", pady=(5, 0))

        self.form_handler.username_entry = tk.Entry(self.form_handler.frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF")
        self.form_handler.username_entry.grid(row=2, column=0, columnspan=2, pady=5)

    def _initialize_password_field(self):
        """Field to write password"""
        tk.Label(master=self.form_handler.frame, text="Salasana", font=("Bookman", 12),
                 fg="#00044A", bg="#D0F1FF").grid(row=3, column=0,
                                                  columnspan=2, sticky="w", pady=(10, 0))

        self.form_handler.password_entry = tk.Entry(master=self.form_handler.frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF", show="*")
        self.form_handler.password_entry.grid(row=4, column=0, columnspan=2, pady=5)

    def _initialize(self):
        self.form_handler.frame = tk.Frame(self._root, bg="#D0F1FF", padx=20, pady=20)
        self.form_handler.frame.place(relx=0.7, rely=0.4, anchor="center")
        Label(self.form_handler.frame, text="Kirjaudu sisään", font=("Bookman", 20, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, columnspan=2, pady=10)

        self.form_handler.error_variable = StringVar(self.form_handler.frame)

        self.form_handler.error_label = tk.Label(master=self.form_handler.frame,
                                     textvariable=self.form_handler.error_variable,
                                     font=("Bookman", 15, "bold"), bg="#D0F1FF", fg="#FC2D7D")
        self.form_handler.error_label.grid(row=0, column=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = tk.Button(master=self.form_handler.frame, text="Kirjaudu sisään",
                                 font=("Bookman", 12), bg="#FADCD9", fg="#00044A", padx=20,
                                 pady=5, borderwidth=0, command=self._login_handler)
        login_button.grid(row=6, column=0, columnspan=2, pady=10)

        registration_button = tk.Button(master=self.form_handler.frame, text="Rekisteröidy tästä",
                                        font=("Bookman", 14, "bold"),
                                        bg="#FADCD9", fg="#00044A", padx=30, pady=8, borderwidth=0,
                                        command=self._handle_registration_view)
        registration_button.grid(row=10, column=0, columnspan=2, pady=10)
