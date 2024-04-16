from UI.sign_up_page import show_sign_up
from UI.login_page import show_login
from tkinter import *
import os

WIN_WIDTH = 720
WIN_HEIGHT = 480
FONT = ("aerial", 8, "bold")


def show_entry_page():
    # Check if there is a users.json file and direct the user to the signup page if not
    if os.path.exists("./Data/users.json"):
        # ASSERT: At least one user has created an account already
        pass

    else:
        print('NO USERS FOUND. TRANSITIONING TO SIGNUP')
        # No users have been created yet, so we can send them straight to the create account page
        show_sign_up()

    # Window
    entry_window = Tk()
    entry_window.config(width=WIN_WIDTH, height=WIN_HEIGHT)  # Sets window size
    entry_window.pack_propagate(False)
    entry_window.minsize(WIN_WIDTH, WIN_HEIGHT)  # Makes sure that the window is at least 720x480

    # Background Image
    background_image = PhotoImage(file='./Assets/lib.png')
    background_label = Label(entry_window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Button Functions
    def transition_to_sign_up() -> None:
        entry_window.destroy()
        show_sign_up()

    def transition_to_login() -> None:
        entry_window.destroy()
        show_login()

    # Buttons
    sign_up_button = Button(text="Sign Up", width=42, command=transition_to_sign_up)
    login_button = Button(text="Login", width=42, command=transition_to_login)

    # Grid
    sign_up_button.place(relx=0.5, rely=0.4, anchor=CENTER)
    login_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    entry_window.mainloop()  # Runs the event loop for the main window
