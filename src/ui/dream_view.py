"""This module includes functions to show dream related view and handle the operations
that can be done on the dream's page"""

from tkinter import Label
import tkinter as tk
from datetime import datetime
from ui.forms import FormHandler
from logic.dreamland_logic import dreamland_logic

class DiaryListView(FormHandler):
    """Class taking care of showing the dream's diary notes"""

    def __init__(self, root, dream, diary):
        super().__init__()
        self._root = root
        self._dream = dream
        self._diary = diary

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self._frame

    def destroy(self):
        """Don't show the window"""
        return self._frame

    def _initialize_diary_note(self, content, created_at, row):
        date = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        date_format = date.strftime("%d-%m-%Y")
        Label(self._frame, text=f"{date_format}: {content}", font=("Bookman", 12),fg="#220066",
              bg="#D0F1FF").grid(row=row, column=0, padx=5, pady=5, sticky="w")

    def _initialize(self):
        self._frame = tk.Frame(self._root, bg="#D0F1FF", padx=10, pady=10)
        self._frame.grid(row=0, column=1, sticky="w", padx=50, pady=50)

        diary = dreamland_logic.get_dream_diary(self._dream.id)
        for r, (content, created_at) in enumerate(diary, start=1):
            self._initialize_diary_note(content, created_at, row=r)

class DreamView(FormHandler):
    """Class taking care of the dream page view and functionalities"""

    def __init__(self, root, dream, handle_show_homepage_view):
        super().__init__()
        self._root = root
        self._dream = dream
        self._handle_show_homepage_view = handle_show_homepage_view
        self._add_note_entry = None
        self._diary_list_frame = None
        self._diary_list_view = None

        self._initialize()

    @property
    def frame(self):
        """Expose _frame via getter"""
        return self._frame

    def destroy(self):
        """Don't show the window"""
        self._frame.destroy()

    def _homepage_handler(self):
        """Returns user back to homepage"""
        self._handle_show_homepage_view()

    def _initialize_diary_list(self):
        if self._diary_list_view:
            self._diary_list_view.destroy()

        for widget in self._diary_list_frame.winfo_children():
            widget.destroy()

        diary = dreamland_logic.get_dream_diary(self._dream.id)

        self._diary_list_view = DiaryListView(self._diary_list_frame, self._dream, diary)

        self._diary_list_view.frame.grid(row=1, column=0, columnspan=2, sticky="nsew",
                                         padx=20, pady=20)

    def _handle_add_note(self):
        """Add a new note to the diary"""
        content = self._add_note_entry.get().strip()
        if content:
            dreamland_logic.new_diary_note(self._dream.id, content)
            self._add_note_entry.delete(0, tk.END)
            self._initialize_diary_list()
            self._root.update_idletasks()

    def _initialize(self):
        self._frame = tk.Frame(self._root, bg="#D0F1FF", padx=20, pady=20)
        self._frame.place(relx=0.5, rely=0.5, anchor="center")

        diary_frame = tk.Frame(self._frame, bg="#D0F1FF")
        diary_frame.grid(row=0, column=0, sticky="nw")

        Label(diary_frame, text=self._dream.content, font=("Bookman", 16, "bold"),
                         fg="#220066", bg="#D0F1FF").grid(
                             row=0, column=0, padx=10, pady=10, sticky="w")

        self._diary_list_frame = tk.Frame(diary_frame, bg="#D0F1FF")
        self._diary_list_frame.grid(row=1, column=0, sticky="nw", padx=10)

        self._initialize_diary_list()
        self._root.update_idletasks()

        add_note_frame = tk.Frame(self._frame, bg="#D0F1FF")
        add_note_frame.grid(row=0, column=1, sticky="ne", padx=(40, 0), pady=(10, 0))

        Label(add_note_frame, text="Mitä tein päästäkseni lähemmäs tavoitettani?",
              font=("Bookman", 12, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self._add_note_entry = tk.Entry(add_note_frame, font=("Bookman", 12), width=30,
                                        borderwidth=2, relief="solid")
        self._add_note_entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        add_note_button = tk.Button(add_note_frame, text="Lisää", font=("Bookman", 12, "bold"),
                                    bg="#FADCD9", fg="#00044A", padx=15, pady=5, borderwidth=0,
                                    relief=tk.FLAT, command=self._handle_add_note)
        add_note_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        homepage_button = tk.Button(self._frame, text="Kotisivulle", font=("Bookman", 14, "bold"),
                                    bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                    command=self._homepage_handler)

        homepage_button.grid(row=1, column=1, sticky="se", padx=10, pady=(30, 0))
