from tkinter import *
from tkinter import messagebox, simpledialog
from tkinter import Tk, Label, Button, Radiobutton, IntVar
from Classes.manager import new_book, search_by_title, check_out_book, check_in_book

WIN_WIDTH = 720
WIN_HEIGHT = 480
FONT = ("aerial", 8, "bold")


def show_main_window(username: str) -> None:

    # Window
    main_window = Tk()
    main_window.config(width=WIN_WIDTH, height=WIN_HEIGHT)  # Sets up win size
    main_window.pack_propagate(False)  # Stops pack() and grid() from resizing the window
    main_window.minsize(WIN_WIDTH, WIN_HEIGHT)  # Makes sure that the window is at least 720x480

    # Background Image
    background_image = PhotoImage(file='./Assets/lib.png')
    background_label = Label(main_window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Button Functions

    def search() -> None:
        # Shows user a pop-up window prompting them to choose their search criteria
        criteria = "Title"  # ask_multiple_choice_question(prompt='Choose search criteria',
        #                   options=['Title', 'Author', 'Series'])

        if criteria == 'Title':
            title = get_question(title='Title', prompt="Please enter the title of the book")
            if title is not None:
                # ASSERT: User didn't try to exit the prompt early
                book_info = search_by_title(title)
                if book_info is not None:
                    # Show the book info in a message box pop-up
                    messagebox.showinfo(title="Book Info",
                                        message=f"Title: {book_info[0].title()}\n\n"
                                                f"Author: {book_info[1].title()}\n\n"
                                                f"Series: {book_info[2].title()}\n\n"
                                                f"Status: {book_info[3].title()}")
                else:
                    # Show error in a message box pop-up
                    messagebox.showinfo(title="Book Info", message="Book not found")

    def check_in() -> None:
        title = get_question(title='Title', prompt="Please enter the title of the book")
        error_code = check_in_book(title=title)
        if error_code == 0:
            messagebox.showinfo(title="Success", message=f"Book has been successfully checked in by {username}")
        elif error_code == 1:
            messagebox.showerror(title="Error", message=f"Book is already checked in")
        else:
            messagebox.showerror(title="Error", message=f"Book not found")

    def check_out() -> None:
        title = get_question(title='Title', prompt="Please enter the title of the book")
        completion_code = check_out_book(title=title, user=username)
        if completion_code == 0:
            messagebox.showinfo(title="Success", message=f"Book has been successfully checked out by {username}")
        elif completion_code == 1:
            messagebox.showerror(title="Error", message=f"Book is already checked out by another user")
        elif completion_code == 2:
            messagebox.showerror(title="Error", message=f"Book not found")

    def add_book() -> None:
        title = get_question(title='Title', prompt="Please enter the title of the book")
        if title is not None:
            # Get the rest of the book info
            author = get_question(title="Author Name", prompt="Enter the author's name")
            series = get_question(title="Series", prompt="Enter the name of the series. Write N/A if not available")
            book_data = {
                title: {
                    "title": title.lower(),
                    "author": author.lower(),
                    "series": series.lower(),
                    "status": "checked in"  # Sets the status to checked in when the book is first added to the system
                }
            }
            new_book(book_data)  # Write the book info to the books.json file

    def remove_book() -> None:
        print("Removing Books")

    def sign_out() -> None:
        main_window.destroy()  # Destroys current window to avoid root window issues
        from UI.entry_page import show_entry_page
        show_entry_page()

    # Buttons
    search_button = Button(text="Search", width=42, command=search)
    check_in_button = Button(text="Check in", width=42, command=check_in)
    check_out_button = Button(text="Check out", width=42, command=check_out)
    add_book_button = Button(text="Add new book", width=42, command=add_book)
    remove_book_button = Button(text="Remove a book", width=42, command=remove_book)
    sign_out_button = Button(text="Sign Out", width=42, command=sign_out)

    # Grid
    '''
                  0         1          2           3
            |----------|----------|----------|----------|
           0|          |  sch(B)  |  sch(B)  |          |
            |----------|----------|----------|----------|
           1|          |   CI(B)  |   CI(B)  |          |
            |----------|----------|----------|----------|
           2|          |   CO(B)  |   CO(B)  |          |
            |----------|----------|----------|----------|
           3|          |   AB(B)  |   AB(B)  |          |
            |----------|----------|----------|----------|
           4|          |   RB(B)  |   RB(B)  |          |
            |----------|----------|----------|----------|
           5|          |   SO(B)  |   SO(B)  |          |
            |----------|----------|----------|----------|
    '''

    search_button.place(relx=0.5, rely=0.1, anchor=CENTER)
    check_in_button.place(relx=0.5, rely=0.25, anchor=CENTER)
    check_out_button.place(relx=0.5, rely=0.4, anchor=CENTER)
    add_book_button.place(relx=0.5, rely=0.55, anchor=CENTER)
    remove_book_button.place(relx=0.5, rely=0.7, anchor=CENTER)
    sign_out_button.place(relx=0.5, rely=0.85, anchor=CENTER)

    main_window.mainloop()


def get_question(title: str, prompt: str) -> str | None:
    result = simpledialog.askstring(title=title, prompt=prompt)  # Prompt user with given prompt
    while result is None or result == '':
        # ASSERT: User didn't enter a response, so we need to re-prompt
        result = simpledialog.askstring(title=title, prompt=prompt)
        if result == 'quit' or result == 'exit' or result is None:  # Check if user is trying to escape the input box
            return None

    return result.lower()  # Return the user's answer as a lowercase string


# **********NOT WORKING********** #
'''
    Issues:
            Always returns the first option even if a different one was selected
            When used multiple times the original window loses its background
'''


def ask_multiple_choice_question(prompt: str, options: list) -> str:
    """
    Displays a pop-up window with a multiple-choice question

    :param prompt: A string to represent the questions being asked
    :param options: A list of strings repressing the options for the user to choose from
    :return: A string representing the selected answer option from the provided list
    """
    root = Tk()  # Create a new window for the radio buttons

    def get_selected_option():
        root.quit()  # Close the window

    if prompt:  # Check s if prompt is not an empty string
        Label(root, text=prompt).pack()  # Creates a label with the prompt
    selected_option_index = IntVar()  # Initialize a variable to store the index of the chosen button
    for i, option in enumerate(options):  # Iterate through the options list
        Radiobutton(root, text=option, variable=selected_option_index, value=i).pack()
    Button(root, text="Submit", command=get_selected_option).pack()  # Creates a submit button that closes the window
    root.mainloop()
    # Only runs once the window is destroyed
    return options[selected_option_index.get()]  # Returns the value of the selected radio button
