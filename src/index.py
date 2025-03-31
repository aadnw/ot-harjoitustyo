from tkinter import Tk, Frame, Label
from UI.ui import ui


def main():
    window = Tk()
    window.title("Haavemaa")
    window.geometry("800x500")
    window.configure(bg="#D0F1FF")
    header = Frame(window, bg="#FADCD9", height=80)
    header.pack(fill="x")
    Label(header, text="Haavemaa", font=("Bookman", 32, "bold"),
          fg="#FF6FA3", bg="#FADCD9").pack(pady=15, padx=20)

    ui_view = ui(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
