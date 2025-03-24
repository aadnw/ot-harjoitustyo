from tkinter import ttk, constants, StringVar
from logic.dreamland_logic import dreamland_logic, InvalidCredentialsError

class LoginView:
    def __init__(self, root, handle_login, handle_show_registration_view):
        self._root = root
        self._handle_login = handle_login
        self._handle_registration_view = handle_show_registration_view
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

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            dreamland_logic.login(username, password)
            self._handle_login()
        except InvalidCredentialsError:
            self._error_message("Virheellinen käyttäjänimi tai salasana")

    def _error_message(self, message):
        self._error_variable.set(message)
        self._error_label.grid()


    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5)        
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_variable = StringVar(self._frame)
        
        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground="orange")
        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(master=self._frame, text="Kirjaudu sisään", command=self._login_handler)
        login_button.grid(padx=5, pady=5, sticky=(constants.E, constants.W), columnspan=2)

        registration_button = ttk.Button(master=self._frame, text="Rekisteröidy", command=self._handle_registration_view)
        registration_button.grid(padx=5, pady=5, sticky=(constants.E, constants.W), columnspan=3)