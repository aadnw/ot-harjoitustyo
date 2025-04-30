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
        date_format = date.strftime("%d.%m.%Y")
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

        if not diary:
            placeholder = tk.Label(self._diary_list_frame, text="",
                                   width=40, height=10, bg="#D0F1FF")
            placeholder.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        else:
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
        """Deletes a dream from the dream list and database,
        asks for confirmation first with a popup window"""
        popup = tk.Toplevel(self._root, bg="#D0F1FF")
        popup.title("Poista haave")
        popup.geometry("400x150")
        popup.transient(self._root)
        popup.grab_set()

        Label(popup, text="Oletko varma, että haluat poistaa haaveen?", font=("Bookman"),
              bg="#D0F1FF", fg="#00044A", pady=20).pack()

        def _yes():
            """Function that is called when user confirms to delete a dream,
            moves user back to homepage after"""
            dreamland_logic.delete_dream(self._dream.id)
            self._handle_show_homepage_view()
            popup.destroy()

        def _no():
            """Function that is called when user doesn't confirm to delete a dream,
            removes the popup window from the view and doesn't delete the dream"""
            popup.destroy()

        self.form_handler.set_buttons_for_confirmation(tk, popup, _yes, _no)

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

        top_frame = tk.Frame(self.form_handler.frame, bg="#D0F1FF")
        top_frame.grid(row=0, column=0, sticky="nsew")

        bottom_frame = tk.Frame(self.form_handler.frame, bg="#D0f1FF")
        bottom_frame.grid(row=1, column=0, sticky="ew", pady=(20, 0))

        diary_frame = tk.Frame(top_frame, bg="#D0F1FF")
        diary_frame.grid(row=0, column=0, sticky="nsew", padx=30, pady=10)

        Label(diary_frame, text=self._dream.content, font=("Bookman", 20, "bold"),
                         fg="#220066", bg="#D0F1FF").grid(row=0, column=0, sticky="w", pady=(0, 20))

        self._diary_list_frame = tk.Frame(diary_frame, bg="#D0F1FF")
        self._diary_list_frame.grid(row=1, column=0, sticky="nsew")

        self._initialize_diary_list()
        self._root.update_idletasks()

        info_frame = tk.Frame(top_frame, bg="#D0F1FF")
        info_frame.grid(row=0, column=1, sticky="ne", padx=30, pady=10)

        days_left = (datetime.strptime(self._dream.due_date, "%d.%m.%Y") - datetime.today()).days

        days_frame = tk.Frame(info_frame, bg="#D0F1FF")
        days_frame.grid(row=0, column=0, pady=(10, 10), sticky="e")

        if days_left < 0:
            due_date_text_label = Label(days_frame, text="Tavoiteaika on ylittynyt",
                               font=("Bookman", 18, "bold"), bg="#D0F1FF", fg="#00044A")
            due_date_text_label.pack(side="left")
        else:
            due_date_number_label = Label(days_frame, text=f"{days_left}",
                                        font =("Bookman", 48, "bold"), fg="#FF0099", bg="#D0F1FF")
            due_date_number_label.pack(side="left")

            due_date_text_label = Label(days_frame, text="päivää jäljellä",
                                font=("Bookman", 18, "bold"), bg="#D0F1FF", fg="#00044A")
            due_date_text_label.pack(side="left")

        self._star_label = Label(info_frame, text=f"Tärkeys: {'★' * int(self._star_value)}/5",
                                 font=("Bookman", 14, "bold"),
                                 bg="#D0F1FF", fg="#00044A")
        self._star_label.grid(row=1, column=0, pady=(0, 10), sticky="e")

        self.combo_var = tk.StringVar(value=str(self._star_value))

        self.combo = tk.OptionMenu(info_frame, self.combo_var,
                                  "1", "2", "3", "4", "5", command=self._star_selection)

        self.combo.config(font=("Bookman", 14, "bold"), bg="#FADCD9", fg="#00044A", padx=10, pady=5)
        menu = self.combo["menu"]
        menu.config(bg="#FADCD9", fg="#00044A", activebackground="#D0F1FF",
                    activeforeground="#00044A")
        self.combo.grid(row=2, column=0, sticky="e")

        Label(bottom_frame, text="Mitä tein päästäkseni lähemmäs tavoitettani?",
              font=("Bookman", 12, "bold"),
              fg="#00044A", bg="#D0F1FF").grid(row=0, column=0, sticky="w", pady=5)

        self.add_note_entry = tk.Entry(bottom_frame, font=("Bookman", 12), width=30,
                                        borderwidth=2, relief="solid")
        self.add_note_entry.grid(row=1, column=0, sticky="w", pady=5)

        add_note_button = tk.Button(bottom_frame, text="Lisää", font=("Bookman", 12, "bold"),
                                    bg="#FADCD9", fg="#00044A", padx=15, pady=5, borderwidth=0,
                                    relief=tk.FLAT, command=self._handle_add_note)
        add_note_button.grid(row=2, column=0, sticky="w", pady=5)

        homepage_button = tk.Button(bottom_frame, text="Kotisivulle",
                                    font=("Bookman", 14, "bold"),
                                    bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                    command=self._homepage_handler)
        homepage_button.grid(row=2, column=1, sticky="e", padx=10)

        delete_button = tk.Button(bottom_frame, text="Poista haave",
                                  font=("Bookman", 14, "bold"),
                                  bg="#FADCD9", fg="#00044A", padx=20, pady=5, borderwidth=0,
                                  command=self._delete_handler)
        delete_button.grid(row=2, column=2, sticky="e", padx=10)

        self.form_handler.frame.grid_columnconfigure(0, weight=1)
        self.form_handler.frame.grid_columnconfigure(1, weight=1)

        diary_frame.grid_rowconfigure(1, weight=1)
        diary_frame.grid_columnconfigure(0, weight=1)

        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=0)
