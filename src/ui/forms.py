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
        """Expose _frame via getter"""
        return self.frame
