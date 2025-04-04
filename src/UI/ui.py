from UI.login_view import LoginView
from UI.homepage_view import HomepageView
from UI.registration_view import RegistrationView


class ui:
    """Luokka, joka vastaa graafisesta käyttöliittymästä"""

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        """Show the login page when starting the application"""
        self._show_login_view()

    def _hide_current_view(self):
        """Hide the current page to show the next page"""
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_login_view(self):
        """Show login page"""
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_homepage_view,
            self._show_registration_view
        )

        self._current_view._frame.grid(row=0, column=0, sticky="nsew")
    def _show_homepage_view(self):
        """Show homepage"""
        self._hide_current_view()

        self._current_view = HomepageView(self._root, self._show_login_view)

        self._current_view._frame.grid(row=0, column=0, sticky="nsew")

    def _show_registration_view(self):
        """Show registration page"""
        self._hide_current_view()

        self._current_view = RegistrationView(
            self._root, self._show_homepage_view, self._show_login_view)

        self._current_view._frame.grid(row=0, column=0, sticky="nsew")