"""This module includes functions to show the login view and handle the operations
that can be done on the login page"""

from tkinter import StringVar, Label
import tkinter as tk
import os
from PIL import Image, ImageTk
from ui.forms import FormHandler
from logic.dreamland_logic import dreamland_logic, InvalidCredentialsError


class LoginView:
    """Class taking care of showing the login page
    
    Attributes:
        root: TKinter element inside of which the view will be initialized
        handle_login: value that is called when logging in the user
        handle_show_registration_view: value that is called when moving to the registration page
    """

    def __init__(self, root, handle_login, handle_show_registration_view):
        """Class taking care of showing the login page
    
        Args:
            root: TKinter element inside of which the view will be initialized
            handle_login: value that is called when logging in the user
            handle_show_registration_view: value that is called when moving to the registration page
        """

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
        self.form_handler.error_variable.set(message)

    def _initialize_username_field(self):
        tk.Label(self.left_frame, text="Käyttäjänimi", font=("Bookman", 12), fg="#00044A",
                 bg="#D0F1FF").grid(row=1, column=0, columnspan=2, sticky="w", pady=(5, 0))

        self.form_handler.username_entry = tk.Entry(self.left_frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF")
        self.form_handler.username_entry.grid(row=2, column=0, columnspan=2, pady=5)

    def _initialize_password_field(self):
        tk.Label(self.left_frame, text="Salasana", font=("Bookman", 12),
                 fg="#00044A", bg="#D0F1FF").grid(row=3, column=0,
                                                  columnspan=2, sticky="w", pady=(10, 0))

        self.form_handler.password_entry = tk.Entry(self.left_frame, width=25, font=(
            "Bookman", 12), bd=2, relief="solid", bg="#DFF7FF", show="*")
        self.form_handler.password_entry.grid(row=4, column=0, columnspan=2, pady=5)

    def _initialize(self):
        self.form_handler.frame = tk.Frame(self._root, bg="#D0F1FF", padx=20, pady=20)
        self.form_handler.frame.place(relx=0.7, rely=0.4, anchor="center")

        left_frame = tk.Frame(self.form_handler.frame, bg ="#D0F1FF")
        left_frame.grid(row=0, column=0, sticky="n")
        self.left_frame = left_frame

        right_frame = tk.Frame(self.form_handler.frame, bg="#D0F1FF")
        right_frame.grid(row=0, column=1, padx=(50, 0), sticky="n")

        Label(left_frame, text="Kirjaudu sisään", font=("Bookman", 20, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, columnspan=2, pady=10)

        self.form_handler.error_variable = StringVar()
        self.form_handler.error_label = tk.Label(right_frame,
                                     textvariable=self.form_handler.error_variable,
                                     font=("Bookman", 15, "bold"), bg="#D0F1FF", fg="#FC2D7D")
        self.form_handler.error_label.grid(row=0, column=0, pady=10)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = tk.Button(left_frame, text="Kirjaudu sisään",
                                 font=("Bookman", 12), bg="#FADCD9", fg="#00044A", padx=20,
                                 pady=5, borderwidth=0, command=self._login_handler)
        login_button.grid(row=6, column=0, columnspan=2, pady=10)

        registration_button = tk.Button(left_frame, text="Rekisteröidy tästä",
                                        font=("Bookman", 14, "bold"),
                                        bg="#FADCD9", fg="#00044A", padx=30, pady=8, borderwidth=0,
                                        command=self._handle_registration_view)
        registration_button.grid(row=10, column=0, columnspan=2, pady=10)

        image_path = os.path.join(os.path.dirname(__file__), "..", "images", "haavemaa_logo.png")
        logo = ImageTk.PhotoImage(Image.open(image_path))
        self.logo_image = logo
        logo_label = Label(right_frame, image=self.logo_image, bg="#D0F1FF")
        logo_label.grid(row=1, column=0, sticky="nsew", padx=60)

        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(1, weight=1)
