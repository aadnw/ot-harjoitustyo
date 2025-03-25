from tkinter import ttk, StringVar, constants
from logic.dreamland_logic import dreamland_logic, UsernameTakenError

class RegistrationView:
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

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _registration_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            dreamland_logic.create_new_user(username, password)
            self._handle_registration()
        except UsernameTakenError:
            self._error_message("Tämä käyttäjänimi on jo käytössä")

    def _error_message(self, message):
        self._error_variable.set(message)
        self._error_label.grid()
    
    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground="orange")
        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        create_button = ttk.Button(master=self._frame, text="Luo käyttäjä", command=self._registration_handler)

        login_button = ttk.Button(master=self._frame, text="Takaisin kirjautumissivulle", command=self._handle_show_login_view)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

        create_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()