"""This module is made to handle form elements for all views,
to avoid too many instance attributes and similar lines"""

class FormHandler:
    """Class for handling form elements"""
    def __init__(self):
        """Class constructor"""
        self.frame = None
        self.dream_list_frame = None
        self.dream_list_view = None
        self.username_entry = None
        self.password_entry = None
        self.error_variable = None
        self.error_label = None

    def destroy(self):
        """Don't show the window"""
        if self.frame:
            self.frame.destroy()

    def show_frame(self):
        """Expose frame"""
        return self.frame

    def set_buttons_for_confirmation(self, tk, popup, _yes, _no):
        """Creates the frame and buttons for the confirmation popup windows
        
        Args:
            tk: tkinter imported as tk
            popup: variable for the popup window
            _yes: function that is called when the yes button is clicked
            _no: function that is called when the no button is clicked
        """
        button_frame = tk.Frame(popup, bg="#D0F1FF")
        button_frame.pack(pady=10)

        yes_button = tk.Button(button_frame, text="Kyllä", font=("Bookman"),
                               bg="#FADCD9", fg="#00044A", width=10, command=_yes)
        yes_button.grid(row=0, column=0, padx=5)

        no_button = tk.Button(button_frame, text="Ei", font=("Bookman"),
                              bg="#FADCD9", fg="#00044A", width=10, command=_no)
        no_button.grid(row=0, column=1, padx=5)
