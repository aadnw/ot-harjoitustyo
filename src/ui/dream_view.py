"""This module includes functions to show dream related view and handle the operations
that can be done on the dream's page"""

from tkinter import Label
import tkinter as tk
from datetime import datetime
from ui.forms import FormHandler
from logic.dreamland_logic import dreamland_logic

class DiaryListView:
    """Class taking care of showing the dream's diary notes
    
    Attributes:
        root: TKinter element inside of which the view will be initialized
        dream: Dream-object of which the view is created
        diary: list of Diary-objects related to the dream
    """

    def __init__(self, root, dream, diary):
        """Class constructor
        
        Args:
            root: TKinter element inside of which the view will be initialized
            dream: Dream-object of which the view is created
            diary: list of Diary-objects related to the dream
        """

        self._root = root
        self._dream = dream
        self._diary = diary
        self.form_handler = FormHandler()

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self.form_handler.show_frame()

    def destroy(self):
        """Don't show the window"""
        return self.form_handler.frame

    def _initialize_diary_note(self, content, created_at, row):
        """Initializes the diary note that will be shown on the Dream-page
        
        Args:
            content: string that describes the content of the note
            created_at: timestamp of the time the note was created at
            row: row number of the note where it will be placed
        """

        date = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        date_format = date.strftime("%d-%m-%Y")
        Label(self.form_handler.frame, text=f"{date_format}: {content}", font=("Bookman", 12),
              fg="#220066", bg="#D0F1FF").grid(row=row, column=0, padx=5, pady=5, sticky="w")

    def _initialize(self):
        """Initializes the view for the diary list"""
        self.form_handler.frame = tk.Frame(self._root, bg="#D0F1FF", padx=10, pady=10)
        self.form_handler.frame.grid(row=0, column=1, sticky="w", padx=50, pady=50)

        diary = dreamland_logic.get_dream_diary(self._dream.id)
        for r, (content, created_at) in enumerate(diary, start=1):
            self._initialize_diary_note(content, created_at, row=r)

class DreamView:
    """Class taking care of the dream page view and functionalities
    
    Attributes:
        root: TKinter element inside of which the view will be initialized
        dream: Dream-object of which the view is created
        handle_show_homepage_view: value that is called when moving to homepage
    """

    def __init__(self, root, dream, handle_show_homepage_view):
        """Class constructor
    
        Args:
            root: TKinter element inside of which the view will be initialized
            dream: Dream-object of which the view is created
            handle_show_homepage_view: value that is called when moving to homepage
        """

        self._root = root
        self._dream = dream
        self._handle_show_homepage_view = handle_show_homepage_view
        self._diary_list_frame = None
        self._diary_list_view = None
        self._star_label = None
        self._star_value = int(str(self._dream.star).split('/', maxsplit=1)[0])

        self.form_handler = FormHandler()

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self.form_handler.show_frame()

    def destroy(self):
        """Don't show the window"""
        self.form_handler.frame.destroy()

    def _homepage_handler(self):
        """Returns user back to homepage"""
        self._handle_show_homepage_view()

    def _initialize_diary_list(self):
        """Initializes the view to show the diary list"""
        if self._diary_list_view:
            self._diary_list_view.destroy()

        for widget in self._diary_list_frame.winfo_children():
            widget.destroy()

        diary = dreamland_logic.get_dream_diary(self._dream.id)

        self._diary_list_view = DiaryListView(self._diary_list_frame, self._dream, diary)

        self._diary_list_view.frame.grid(row=1, column=0, columnspan=2, sticky="nsew",
                                         padx=20, pady=20)

    def _handle_add_note(self):
        """Adds a new note to the diary"""
        content = self.add_note_entry.get().strip()
        if content:
            dreamland_logic.new_diary_note(self._dream.id, content)
            self.add_note_entry.delete(0, tk.END)
            self._initialize_diary_list()
            self._root.update_idletasks()

    def _delete_handler(self):
        """Deletes a dream from the dream list and database"""
        dreamland_logic.delete_dream(self._dream.id)
        self._handle_show_homepage_view()

    def _star_selection(self, value):
        """Sets the new star value for the chosen dream
        
        Args:
            value: integer that describes the new star value of the dream
        """

        set_star = int(value)
        self._star_value = set_star
        self._star_label.config(text=f"Tärkeys: {'★' * set_star}/5")

        dreamland_logic.dream_star(self._dream.id, set_star)

    def _initialize(self):
        """Initializes the dream page's ui"""
        self.form_handler.frame = tk.Frame(self._root, bg="#D0F1FF", padx=20, pady=20)
        self.form_handler.frame.grid(row=0, column=0, sticky="nsew")

        diary_frame = tk.Frame(self.form_handler.frame, bg="#D0F1FF")
        diary_frame.grid(row=0, column=0, sticky="n", padx=30)

        self.combo_var = tk.StringVar(value=str(self._star_value))

        self.combo = tk.OptionMenu(self.form_handler.frame, self.combo_var,
                                  "1", "2", "3", "4", "5", command=self._star_selection)

        self.combo.config(font=("Bookman", 14, "bold"), bg="#FADCD9", fg="#00044A", padx=10, pady=5)
        menu = self.combo["menu"]
        menu.config(bg="#FADCD9", fg="#00044A", activebackground="#D0F1FF",
                    activeforeground="#00044A")
        self.combo.grid(row=3, column=1, sticky="se", padx=10, pady=(30, 0))

        Label(diary_frame, text=self._dream.content, font=("Bookman", 16, "bold"),
                         fg="#220066", bg="#D0F1FF").pack(anchor="w", pady=(0, 20))

        self._diary_list_frame = tk.Frame(diary_frame, bg="#D0F1FF")
        self._diary_list_frame.pack(anchor="w")

        self._initialize_diary_list()
        self._root.update_idletasks()

        add_note_frame = tk.Frame(self.form_handler.frame, bg="#D0F1FF")
        add_note_frame.grid(row=0, column=1, sticky="ne", padx=30)

        Label(add_note_frame, text="Mitä tein päästäkseni lähemmäs tavoitettani?",
              font=("Bookman", 12, "bold"),
              fg="#00044A", bg="#D0F1FF").pack(anchor="w", pady=(0, 5))

        self.add_note_entry = tk.Entry(add_note_frame, font=("Bookman", 12), width=30,
                                        borderwidth=2, relief="solid")
        self.add_note_entry.pack(anchor="w", pady=(0, 5))

        add_note_button = tk.Button(add_note_frame, text="Lisää", font=("Bookman", 12, "bold"),
                                    bg="#FADCD9", fg="#00044A", padx=15, pady=5, borderwidth=0,
                                    relief=tk.FLAT, command=self._handle_add_note)
        add_note_button.pack(anchor="w", pady=(0, 30))

        self._star_label = Label(add_note_frame, text=f"Tärkeys: {'★' * int(self._star_value)}/5",
                                 font=("Bookman", 14, "bold"),
                                 bg="#D0F1FF", fg="#00044A")
        self._star_label.pack(anchor="e", pady=(0, 10))

        homepage_button = tk.Button(self.form_handler.frame, text="Kotisivulle",
                                    font=("Bookman", 14, "bold"),
                                    bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                    command=self._homepage_handler)

        homepage_button.grid(row=1, column=1, sticky="se", padx=10, pady=(30, 0))

        delete_button = tk.Button(self.form_handler.frame, text="Poista haave",
                                  font=("Bookman", 14, "bold"),
                                  bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                  command=self._delete_handler)

        delete_button.grid(row=2, column=1, sticky="se", padx=10, pady=(30, 0))

        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)
