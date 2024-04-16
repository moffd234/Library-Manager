from tkinter import *
from tkinter import messagebox
from Classes.manager import search_users

WIN_WIDTH = 720
WIN_HEIGHT = 480
FONT = ("aerial", 8, "bold")


def show_login():

    # Window
    login_window = Tk()
    login_window.config(width=WIN_WIDTH, height=WIN_HEIGHT)  # Adds padding and sets up win size
    login_window.pack_propagate(False)  # Stops pack() and grid() from resizing the window
    login_window.minsize(WIN_WIDTH, WIN_HEIGHT)  # Makes sure that the window is at least 720x480

    # Background Image
    background_image = PhotoImage(file='./Assets/lib.png')
    background_label = Label(login_window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Labels
    login_label = Label(master=login_window, text="LOGIN", bg="burlywood2", font=FONT)
    username_label = Label(master=login_window, text='Username', bg="burlywood2", font=FONT)
    password_label = Label(master=login_window, text='Password', bg="burlywood2", font=FONT)

    # Entries
    username_entry = Entry(width=51, bg="burlywood1", highlightthickness=0, font=FONT)
    username_entry.focus()  # Makes it so that the username field is pre-selected
    password_entry = Entry(width=51, bg="burlywood1", highlightthickness=0, font=FONT)

    # Button Functions
    def login_pressed():
        un = username_entry.get().lower()
        pw = password_entry.get().lower()

        if un == '' or pw == '':
            messagebox.showerror(title="Field Error", message='Please fill out all fields')
        else:
            login_info = search_users(un)  # Gets the login info for the given username if applicable
            if login_info is None or un != login_info[0] or pw != login_info[1]:
                # ASSERT: The provided username and password are not valid
                messagebox.showerror(title='User not found', message='Username and/or password is incorrect')
            else:
                # ASSERT: User entered a valid username and password
                from UI.main_page_ui import show_main_window
                login_window.destroy()  # Kill current window first to avoid root window issues
                show_main_window(username=un)  # Transition to main view

    # Button
    login_button = Button(text="Login", width=42, command=login_pressed)

    # Grid
    '''
                  0         1          2           3
            |----------|----------|----------|----------|
           0|          |   LI(L)  |          |          |
            |----------|----------|----------|----------|
           1|   UN(L)  |   UN(E)  |   UN(E)  |          |
            |----------|----------|----------|----------|
           2|   PW(L)  |   PW(E)  |   PW(E)  |          |
            |----------|----------|----------|----------|
           3|          |   LI(B)  |   LI(B)  |          |
            |----------|----------|----------|----------|
    '''

    login_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    username_label.place(relx=0.2, rely=0.4, anchor=CENTER)
    password_label.place(relx=0.2, rely=0.6, anchor=CENTER)
    username_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
    password_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
    login_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    login_window.mainloop()
