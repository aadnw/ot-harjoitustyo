from tkinter import constants, Label
import tkinter as tk
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
        self._frame = tk.Frame(self._root, bg="#D0F1FF", padx=20, pady=20)
        self._frame.place(relx=0.7, rely=0.4, anchor="center")

        user = dreamland_logic.get_user()
        Label(self._frame, text=f"Tervetuloa Haavemaahan {user.username} <3", font=("Bookman", 20, "bold"), fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, columnspan=2, pady=10)
        
        logout_button = tk.Button(master=self._frame, text="Kirjaudu ulos", font=("Bookman", 12), bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0, command=self._logout_handler)
        logout_button.grid(row=1, column=0, padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=400)