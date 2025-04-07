"""This module creates the main window for the application"""

from tkinter import Tk, Frame, Label
from UI.ui import UI

def main():
    """Creates the application window"""
    window = Tk()
    window.title("Haavemaa")
    window.minsize(800, 500)
    window.configure(bg="#D0F1FF")

    header = Frame(window, bg="#FADCD9", height=80)
    header.pack(fill="x")
    Label(header, text="Haavemaa", font=("Bookman", 32, "bold"),
          fg="#FF6FA3", bg="#FADCD9").pack(pady=15, padx=20)

    content_frame = Frame(window, bg="#D0F1FF")
    content_frame.pack(fill="both", expand=True)

    ui_view = UI(content_frame)
    ui_view.start()

    window.update_idletasks()

    window.mainloop()

if __name__ == "__main__":
    main()
