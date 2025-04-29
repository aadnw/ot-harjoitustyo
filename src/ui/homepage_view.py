"""This module includes functions to show the homepage view and handle the operations
that can be done on the homepage"""

from tkinter import Label
import tkinter as tk
from datetime import datetime
from inspirational_quotes import quote
from tkcalendar import DateEntry
from ui.forms import FormHandler
from logic.dreamland_logic import dreamland_logic


class DreamListView:
    """Class taking care of showing the users' dreams
    
    Attributes:
        root: TKinter element inside of which the view will be initialized
        dreams: list of Dream-objects that will be shown on the homepage
        handle_set_dream_achieved: value that is called when a dream is marked as achieved,
        gets id of the achieved dream as argument
        handle_show_dream_view: value that is called when moving to dream-page
    """

    def __init__(self, root, dreams, handle_set_dream_achieved, handle_show_dream_view):
        """Class constructor
    
        Args:
            root: TKinter element inside of which the view will be initialized
            dreams: list of Dream-objects that will be shown on the homepage
            handle_set_dream_achieved: value that is called when a dream is marked as achieved,
            gets id of the achieved dream as argument
            handle_show_dream_view: value that is called when moving to dream-page
        """

        self._root = root
        self._dreams = dreams
        self._handle_set_dream_achieved = handle_set_dream_achieved
        self._handle_show_dream_view = handle_show_dream_view
        self.form_handler = FormHandler()

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self.form_handler.show_frame()

    def destroy(self):
        """Don't show the window"""
        self.form_handler.frame.destroy()

    def _initialize_dream_item(self, dream, row):
        """Initializes the dreams that will be shown on the homepage
        
        Args:
            dream: Dream-object to be initialized
            row: integer that describes the row where the dream will be placed
        """

        label = tk.Label(self.form_handler.frame, text=dream.content, font=(
            "Bookman", 12), fg="#220066", bg="#D0F1FF")
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

        dream_page_button = tk.Button(self.form_handler.frame, text="Edistyminen",
                                      font=("Bookman", 10, "bold"),
                                      bg="#FBBFCA", fg="#00044A", padx=10, pady=5, borderwidth=0,
                                      relief=tk.FLAT,
                                      command=lambda d=dream: self._handle_show_dream_view(d))
        dream_page_button.grid(row=row, column=1, padx=10, pady=5, sticky="e")

        achieved_button = tk.Button(self.form_handler.frame, text="Saavutettu",
                                    font=("Bookman", 10, "bold"),
                                    bg="#E2F89C", fg="#00044A", padx=10, pady=5, borderwidth=0,
                                    relief=tk.FLAT, command=lambda dream=dream:
                                    self._handle_set_dream_achieved(dream.id))
        achieved_button.grid(row=row, column=2, padx=10, pady=5, sticky="e")

    def _dream_order(self, order):
        """Function that puts the dreams into the given order
        
        Args:
            order: string that describes the order for the dreams
        """

        if order == "Tärkeimmät ensin":
            self._dreams.sort(key=lambda d: d.star, reverse=True)
        if order == "Tavoiteaika ensin":
            self._dreams.sort(key=lambda d: datetime.strptime(d.due_date, "%d.%m.%Y"))
        if order == "Uusin ensin":
            self._dreams.sort(key=lambda d: d.id, reverse=True)
        if order == "Vanhin ensin":
            self._dreams.sort(key=lambda d: d.id)

        for widget in self.form_handler.frame.winfo_children():
            info = widget.grid_info()
            if info.get("row") != 0:
                widget.destroy()

        for r, dream in enumerate(self._dreams, start=1):
            self._initialize_dream_item(dream, row=r)


    def _initialize(self):
        """Initializes the dream list to be shown on the homepage"""
        self.form_handler.frame = tk.Frame(self._root, bg="#D0F1FF", padx=10, pady=10)
        self.form_handler.frame.grid(row=0, column=1, sticky="n", padx=50, pady=20)

        Label(self.form_handler.frame, text="Haaveet ja tavoitteet:", font=("Bookman", 14, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, columnspan=2, sticky="nw",
                                               padx=5, pady=(5, 0))

        self.combo_var = tk.StringVar(value="Järjestä")

        self.combo = tk.OptionMenu(self.form_handler.frame, self.combo_var,
                                  "Tärkeimmät ensin", "Tavoiteaika ensin", "Uusin ensin",
                                  "Vanhin ensin", command=self._dream_order)

        self.combo.config(font=("Bookman", 10), bg="#FADCD9", fg="#00044A", padx=10, pady=5)
        menu = self.combo["menu"]
        menu.config(bg="#FADCD9", fg="#00044A", activebackground="#D0F1FF",
                    activeforeground="#00044A")
        self.combo.grid(row=0, column=2, sticky="ne", padx=5, pady=(5, 0))

        dreams = dreamland_logic.get_unachieved_dreams()
        for r, dream in enumerate(dreams, start=1):
            self._initialize_dream_item(dream, row=r)


class HomepageView:
    """Class taking care of the homepage view and functionalities
    
    Attributes:
        root: TKinter element inside of which the view will be initialized
        handle_loogut: value that is called when logging out the user
        handle_show_dream_view: value that is called when moving to the dream-page
    """

    def __init__(self, root, handle_logout, handle_show_dream_view):
        """Class taking care of the homepage view and functionalities
    
        Args:
            root: TKinter element inside of which the view will be initialized
            handle_loogut: value that is called when logging out the user
            handle_show_dream_view: value that is called when moving to the dream-page
        """
        self._root = root
        self._handle_logout = handle_logout
        self._handle_show_dream_view = handle_show_dream_view
        self._add_dream_entry = None
        self.form_handler = FormHandler()

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self.form_handler.show_frame()

    def destroy(self):
        """Don't show the window"""
        self.form_handler.frame.destroy()

    def _logout_handler(self):
        """Logs out the user"""
        dreamland_logic.logout()
        self._handle_logout()

    def _delete_user_handler(self):
        """Deletes the current user from the database,
        asks for confirmation with a popup window first"""
        popup = tk.Toplevel(self._root, bg="#D0F1FF")
        popup.title("Poista käyttäjätunnukset")
        popup.geometry("400x150")
        popup.transient(self._root)
        popup.grab_set()

        Label(popup, text="Oletko varma, että haluat poistaa käyttäjäsi?", font=("Bookman"),
              bg="#D0F1FF", fg="#00044A", pady=20).pack()

        def _yes():
            """Function that is called when user confirms to delete their user credentials,
            moves user back to login page after"""
            user = dreamland_logic.get_user()
            dreamland_logic.delete_user(user.user_id)
            self._logout_handler()
            popup.destroy()

        def _no():
            """Function that is called when user doesn't confirm to delete their user credentials,
            removes the popup window from the view and doesn't delete the user's credentials"""
            popup.destroy()

        self.form_handler.set_buttons_for_confirmation(tk, popup, _yes, _no)

    def _dream_view_handler(self, dream):
        """Shows the dream page
        Args:
            dream: Dream-object that tells which dream's page should be opened
        """

        self._handle_show_dream_view(dream)

    def _handle_set_dream_achieved(self, dream_id):
        """Marks dream as achieved and removes it from the view
        
        Args:
            dream_id: integer that describes the id of the dream that will be set as achieved
        """

        dreamland_logic.dream_achieved(dream_id)
        self._initialize_dream_list()
        self._root.update_idletasks()

    def _initialize_dream_list(self):
        """Initializes the dream list view to be shown on the homepage"""
        if self.form_handler.dream_list_view:
            self.form_handler.dream_list_view.destroy()

        for widget in self.form_handler.dream_list_frame.winfo_children():
            widget.destroy()

        dreams = dreamland_logic.get_unachieved_dreams()

        self.form_handler.dream_list_view = DreamListView(
            self.form_handler.dream_list_frame, dreams, self._handle_set_dream_achieved,
            self._handle_show_dream_view)

        self.form_handler.dream_list_view.frame.grid(
            row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

    def _handle_add_dream(self):
        """Adds a new dream and shows it on the homepage"""
        content = self._add_dream_entry.get().strip()
        due_date = self._add_due_date_entry.get_date().strftime("%d.%m.%Y")

        if content:
            dreamland_logic.new_dream(content, due_date)
            self._add_dream_entry.delete(0, tk.END)
            self._add_due_date_entry.set_date(datetime.today())
            self._initialize_dream_list()
            self._root.update_idletasks()

    def _initialize(self):
        "Initializes the homepage's ui"
        self.form_handler.frame = tk.Frame(self._root, bg="#D0F1FF", padx=30, pady=30)
        self.form_handler.frame.place(relx=0.5, rely=0.5, anchor="center")

        content_frame = tk.Frame(self.form_handler.frame, bg="#D0F1FF")
        content_frame.grid(row=0, column=0, sticky="nw")

        user = dreamland_logic.get_user()
        Label(content_frame, text=f"Tervetuloa Haavemaahan {user.username} <3",
              font=("Bookman", 20, "bold"), fg="#00044A",
              bg="#D0F1FF").grid(row=0, column=0, sticky="nw", columnspan=2, pady=(0, 20))

        quote_frame = tk.Frame(content_frame, bg="#D0F1FF")
        quote_frame.grid(row=1, column=0, sticky="nw")

        self.quote = quote()
        Label(quote_frame, text='"' + self.quote['quote'] + '"' + ' -' + self.quote['author'],
              font=("Bookman", 15), fg="#00044A", bg="#D0F1FF", wraplength=400,
              justify="left").grid(row=0, column=0, pady=(0, 40), sticky="nw")

        add_dream_frame = tk.Frame(content_frame, bg="#D0F1FF")
        add_dream_frame.grid(row=2, column=0, sticky="w", pady=(20, 20))

        Label(add_dream_frame, text="Lisää tavoite:", font=("Bookman", 12, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self._add_dream_entry = tk.Entry(
            add_dream_frame, font=("Bookman", 12), width=30, borderwidth=2, relief="solid")
        self._add_dream_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        Label(add_dream_frame, text="Aseta tavoiteaika:", font=("Bookman", 12, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self._add_due_date_entry = DateEntry(add_dream_frame, font=("Bookman", 12), width=10,
                                             date_pattern="dd.mm.yyyy", mindate=datetime.today(),
                                             background="#D0F1FF", foreground="#00044A",
                                             selectbackground="#FC2D7D", selectforeground="00044A",
                                             bordercolor="#FC2D7D", headersbackground="#D0F1FF",
                                             headersforeground="#00044A",
                                             normalbackground="#FADCD9", normalforeground="#00044A",
                                             weekendbackground="#EC838C",
                                             weekendforeground="#00044A",
                                             othermonthbackground="#D0F1FF",
                                             othermonthforeground="#00044A"
                                             )
        self._add_due_date_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        create_new_dream_button = tk.Button(add_dream_frame, text="Luo",
                                            font=("Bookman", 12, "bold"), bg="#FADCD9",
                                            fg="#00044A", padx=15, pady=5, borderwidth=0,
                                            relief=tk.FLAT, command=self._handle_add_dream)
        create_new_dream_button.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.form_handler.dream_list_frame = tk.Frame(self.form_handler.frame, bg="#D0F1FF")
        self.form_handler.dream_list_frame.grid(
            row=0, column=1, sticky="n", padx=40)

        self._initialize_dream_list()
        self._root.update_idletasks()

        button_frame = tk.Frame(content_frame, bg="#D0F1FF")
        button_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="w")

        logout_button = tk.Button(button_frame, text="Kirjaudu ulos",
                                  font=("Bookman", 12, "bold"), bg="#FADCD9", fg="#00044A",
                                  padx=20, pady=5, borderwidth=0, relief=tk.FLAT,
                                  command=self._logout_handler)
        logout_button.pack(side="left", padx=(0, 10))

        delete_user_button = tk.Button(button_frame, text="Poista käyttäjä",
                                       font=("Bookman", 12, "bold"), bg="#FADCD9", fg="#00044A",
                                       padx=20, pady=5, borderwidth=0, relief=tk.FLAT,
                                       command=self._delete_user_handler)
        delete_user_button.pack(side="left")

        self.form_handler.frame.grid_columnconfigure(0, weight=1)
        self.form_handler.frame.grid_columnconfigure(1, weight=1)
        self.form_handler.frame.grid_rowconfigure(1, weight=1)
