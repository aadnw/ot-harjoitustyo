from tkinter import ttk, constants
from logic.dreamland_logic import dreamland_logic

class HomepageView:
    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        dreamland_logic.logout()
        self._handle_logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label = ttk.Label(self._frame, text="Tervetuloa Haavemaahan <3")
        
        logout_button = ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self._logout_handler)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)

        logout_button.grid(padx=5, pady=5, sticky=constants.EW)
        label.grid(padx=5, pady=5)
