from tkinter import constants, Label
import tkinter as tk
from logic.dreamland_logic import dreamland_logic

class DreamListView:
    """Class taking care of listing the dreams on the homepage"""

    def __init__(self, root, dreams, handle_set_dream_achieved):
        self._root = root
        self._dreams = dreams
        self._handle_set_dream_achieved = handle_set_dream_achieved
        self._frame = None

        self._initialize()

    def pack(self):
        """Show the window"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Don't show the window"""
        self._frame.destroy()

    def _initialize_dream_item(self, dream):
        """Show the dreams on the homepage"""
        item_frame = tk.Frame(self._frame, bg="#D0F1FF")
        label = tk.Label(item_frame, text=dream.content, font=("Bookman", 12), fg="#220066", bg="#D0F1FF")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        achieved_button = tk.Button(item_frame, text="Saavutus", font=("Bookman", 10, "bold"), bg="#FADCD9", fg="#00044A", padx=10, pady=5, borderwidth=0, relief=tk.FLAT,
                                    command=lambda d=dream: self._handle_set_dream_achieved(d.id))
        achieved_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = tk.Frame(self._root)

        for dream in self._dreams:
            self._initialize_dream_item(dream)


class HomepageView:
    """Class taking care of showing content on the homepage"""

    def __init__(self, root, handle_logout):
        self._root = root
        self._handle_logout = handle_logout
        self._user = dreamland_logic.get_user()
        self._frame = None
        self._add_dream_entry = None
        self._dream_list_frame = None
        self._dream_list_view = None

        self._initialize()

    def pack(self): 
        """Show the window"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Don't show the window"""
        self._frame.destroy()

    def _logout_handler(self):
        """Log out the user"""
        dreamland_logic.logout()
        self._handle_logout()

    def _handle_set_dream_achieved(self, dream_id):
        """Mark dream as achieved and remove it from the view"""
        dreamland_logic.dream_achieved(dream_id)
        self._initialize_dream_list()

    def _initialize_dream_list(self):
        if self._dream_list_frame:
            for widget in self._dream_list_frame.winfo_children():
                widget.destroy()

        dream_list_frame = tk.Frame(self._frame, bg="#D0F1FF")
        dream_list_frame.grid(row=1, column=1, sticky="ne", padx=20, pady=20)

        Label(dream_list_frame, text="Haaveet ja tavoitteet:", font=("Bookman", 14, "bold"), fg="#220066", bg="#D0F1FF").pack(anchor="w")

        dreams = dreamland_logic.get_unachieved_dreams()

        for dream in dreams:
            dream_frame = tk.Frame(dream_list_frame, bg="#D0F1FF")
            dream_frame.pack(fill=tk.X, pady=5)

            tk.Label(dream_frame, text=dream.content, font=("Bookman", 12), fg="#220066", bg="#D0F1FF").pack(side="left", padx=5)
            tk.Button(dream_frame, text="Saavutus", font=("Bookman", 10, "bold"), bg="#FADCD9", fg="#00044A", padx=10, pady=5, borderwidth=0, relief=tk.FLAT,
                                    command=lambda d_id=dream.id: self._handle_set_dream_achieved(d_id)).pack(side="right", padx=10)

    def _handle_add_dream(self):
        """Add a new dream and show it on the homepage"""
        content = self._add_dream_entry.get().strip()
        if content:
            dreamland_logic.new_dream(content)
            self._add_dream_entry.delete(0, tk.END)
            self._initialize_dream_list()

    def _initialize(self):
        self._frame = tk.Frame(self._root, bg="#D0F1FF", padx=30, pady=30)
        self._frame.pack(fill="both", expand=True)

        self._dream_list_frame = tk.Frame(self._frame, bg="#D0F1FF")
        self._dream_list_frame.grid(row=1, column=1, sticky="ne", padx=20, pady=20)

        user = dreamland_logic.get_user()
        Label(self._frame, text=f"Tervetuloa Haavemaahan {user.username} <3",
              font=("Bookman", 20, "bold"), fg="#00044A",
              bg="#D0F1FF").grid(row=0, column=0, sticky="w", columnspan=2, pady=10)

        Label(self._dream_list_frame, text="Haaveet ja tavoitteet:",
              font=("Bookman", 14, "bold"), fg="#00044A",
              bg="#D0F1FF").pack(anchor="w")
        
        self._initialize_dream_list()

        user = dreamland_logic.get_user()
        Label(self._frame, text=f"Tervetuloa Haavemaahan {user.username} <3",
              font=("Bookman", 20, "bold"), fg="#00044A",
              bg="#D0F1FF").grid(row=0, column=0, sticky="w", columnspan=2, pady=10)

        add_dream_frame = tk.Frame(self._frame, bg="#D0F1FF")
        add_dream_frame.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="w")

        Label(add_dream_frame, text="Lisää tavoite:", font=("Bookman", 12, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, padx=10, pady=10)

        self._add_dream_entry = tk.Entry(
            add_dream_frame, font=("Bookman", 12), width=30, borderwidth=2, relief="solid")
        self._add_dream_entry.grid(row=0, column=1, padx=10, pady=10)

        create_new_dream_button = tk.Button(add_dream_frame, text="Luo", font=("Bookman", 12, "bold"),
                                            bg="#FADCD9", fg="#00044A", padx=15, pady=5, borderwidth=0,
                                            relief=tk.FLAT, command=self._handle_add_dream)
        create_new_dream_button.grid(row=0, column=2, padx=10, pady=10)

        logout_button = tk.Button(master=self._frame, text="Kirjaudu ulos",
                                  font=("Bookman", 12), bg="#FADCD9", fg="#00044A",
                                  padx=20, pady=5, borderwidth=0, relief=tk.FLAT,
                                  command=self._logout_handler)
        logout_button.grid(row=3, column=1, padx=20, pady=15, sticky="e")

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
