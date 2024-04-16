from tkinter import *
from tkinter import messagebox
from Classes.manager import add_user

WIN_WIDTH = 720
WIN_HEIGHT = 480
FONT = ("aerial", 8, "bold")


def show_sign_up() -> None:
    """
        Displays the sign-up page UI for user registration.

        This function creates a new window with sign-up related widgets including labels, entry fields, and buttons.
        Users can enter their information, and upon clicking the "Sign Up" button, the data is validated and stored
        if it meets the criteria. If successful, the user is redirected to the entry page.

        Returns:
            None
        """
    # Window
    sign_up_window = Tk()  # Creates main window for the sign_up page
    sign_up_window.config(width=WIN_WIDTH, height=WIN_HEIGHT)  # Adds padding and sets up win size
    sign_up_window.pack_propagate(False)  # Stops pack() and grid() from resizing the window
    sign_up_window.minsize(WIN_WIDTH, WIN_HEIGHT)  # Makes sure that the window is at least 720x480

    # Background Image
    bg_image = PhotoImage(file='./Assets/lib.png')
    bg_label = Label(sign_up_window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Labels
    sign_up_label = Label(master=sign_up_window, text="SIGN UP", bg="burlywood2", font=FONT)
    fname_label = Label(master=sign_up_window, text='First Name', bg="burlywood2", font=FONT)
    lname_label = Label(master=sign_up_window, text='Last Name', bg="burlywood2", font=FONT)
    username_label = Label(master=sign_up_window, text='Username', bg="burlywood2", font=FONT)
    password_label = Label(master=sign_up_window, text='Password', bg="burlywood2", font=FONT)
    confirm_label = Label(master=sign_up_window, text='Confirm Password', bg="burlywood2", font=FONT)

    # Entries
    fname_entry = Entry(width=50, bg="burlywood1", font=FONT)
    fname_entry.focus()  # Makes it so that the name field is pre-selected
    lname_entry = Entry(width=50, bg="burlywood1", font=FONT)
    username_entry = Entry(width=50, bg="burlywood1", font=FONT)
    password_entry = Entry(width=50, bg="burlywood1", font=FONT)
    confirm_entry = Entry(width=50, bg='burlywood1', font=FONT)

    # Button Functions
    def sign_up_pressed() -> None:
        if not do_passwords_match(first_password=password_entry.get(),
                                  second_password=confirm_entry.get()):
            # ASSERT: Passwords do not match, so we must throw an error
            messagebox.showerror(title="Password Error",
                                 message="The password and confirm password fields do not match")

        else:
            # Store the text from all the entries in their own variables
            un = username_entry.get()
            fname = fname_entry.get()
            lname = lname_entry.get()
            pw = password_entry.get()
            if is_empty(un, fname, lname, pw):
                # ASSERT: Not all fields are filled out, so we should throw an error
                # asking the user to fill out all fields
                messagebox.showerror(title="Field Error",
                                     message="Not all fields are filled out. Please finish filling out the fields")
            else:
                # Store all the data into a dictionary then write the dictionary to users.json
                usr_data = {
                    un: {
                        "fname": fname,
                        "lname": lname,
                        "username": un,
                        "pwd": pw
                    }
                }
                add_user(usr_data)
                from UI.entry_page import show_entry_page
                sign_up_window.destroy()
                show_entry_page()

    # Button
    sign_up_button = Button(text="Sign Up", width=42, command=sign_up_pressed)

    # Grid
    '''
    
                  0         1          2           3
            |----------|----------|----------|----------|
           0|          |   SU(L)  |   SU(L)  |          |
            |----------|----------|----------|----------|
           1|   FN(L)  |   FN(E)  |   FN(E)  |          |
            |----------|----------|----------|----------|
           2|   LN(L)  |   LN(E)  |   LN(E)  |          |
            |----------|----------|----------|----------|
           3|   UN(L)  |   UN(E)  |   UN(E)  |          |
            |----------|----------|----------|----------|
           4|   PW(L)  |   PW(E)  |   PW(E)  |   GEN(B) |
            |----------|----------|----------|----------|
           5|   CPW(L) |   CPW(E) |  CPW(E)  |          |
            |----------|----------|----------|----------|
           6|          |   SU(B)  |   SU(B)  |          |
            |----------|----------|----------|----------|
    
    '''
    # Place widgets in the center
    sign_up_label.place(relx=0.5, rely=0.1, anchor=CENTER)
    fname_label.place(relx=0.2, rely=0.3, anchor=CENTER)
    lname_label.place(relx=0.2, rely=0.4, anchor=CENTER)
    username_label.place(relx=0.2, rely=0.5, anchor=CENTER)
    password_label.place(relx=0.2, rely=0.6, anchor=CENTER)
    confirm_label.place(relx=0.2, rely=0.7, anchor=CENTER)

    fname_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
    lname_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
    username_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
    password_entry.place(relx=0.5, rely=0.6, anchor=CENTER)
    confirm_entry.place(relx=0.5, rely=0.7, anchor=CENTER)

    sign_up_button.place(relx=0.5, rely=0.85, anchor=CENTER)

    sign_up_window.mainloop()


def do_passwords_match(first_password: str, second_password: str) -> bool:
    return first_password == second_password  # Returns a boolean value representing if the passwords match


def is_empty(*args) -> bool:
    # Loop through the args and return true if any fields are empty
    for entry in args:
        if entry == '' or entry == ' ':
            return True
    return False
