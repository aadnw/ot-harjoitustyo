"""This module is made to handle form elements for all views,
to avoid too many instance attributes and similar lines"""

class FormHandler:
    """Class for handling form elements"""
    def __init__(self):
        self._frame = None
        self._dream_list_frame = None
        self._dream_list_view = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

    def destroy(self):
        """Don't show the window"""
        if self._frame:
            self._frame.destroy()
