import json


def add_user(usr_data: dict):
    try:
        with open(file='./Data/users.json', mode='r') as data_file:
            # ASSERT: users.json is already created
            data = json.load(data_file)  # Loads the current data in the JSON file

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # ASSERT: File was not readable either because it didn't exist or was empty
        with open(file='./Data/users.json', mode='w') as data_file:
            json.dump(usr_data, data_file, indent=4)  # Dumps usr_data to the data file

    else:
        # ASSERT: No error was thrown
        data.update(usr_data)
        with open(file='./Data/users.json', mode='w') as data_file:
            json.dump(data, data_file, indent=4)  # Writes the password to the password file


def search_users(username) -> tuple | None:
    try:
        with open(file='./Data/users.json', mode='r') as data_file:
            # Load the user.json file data then search it for the username provided
            users = json.load(fp=data_file)
            un = users[username]["username"].lower()
            pwd = users[username]["pwd"].lower()
            return un, pwd

    except (FileNotFoundError, KeyError) as error:
        # ASSERT: Either the file doesn't exist or the username doesn't exist
        print(f"The following error occurred in search_users:\n{error}")
        return None  # Return none since the user doesn't exist in the users.json file


def new_book(book_info: dict) -> None:
    try:
        with open(file='./Data/books.json', mode='r') as data_file:
            # ASSERT: users.json is already created
            data = json.load(data_file)  # Loads the current data in the JSON file

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # ASSERT: File was not readable either because it didn't exist or was empty
        with open(file='./Data/books.json', mode='w') as data_file:
            json.dump(book_info, data_file, indent=4)  # Dumps usr_data to the data file

    else:
        # ASSERT: No error was thrown
        data.update(book_info)
        with open(file='./Data/books.json', mode='w') as data_file:
            json.dump(data, data_file, indent=4)  # Writes the password to the password file


def search_by_title(title) -> tuple | None:
    try:
        with open(file='./Data/books.json', mode='r') as data_file:
            data = json.load(fp=data_file)  # Load the books.json file
            title = data[title]['title']  # Get the title for the given book
            author = data[title]['author']  # Get the author for the given book
            series = data[title]['series']  # Get the series for the given book
            status = data[title]['status']  # Get the status for the given book
            return title, author, series, status  # Return title and author as a tuple

    except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError) as error:
        # ASSERT: Website doesn't exist in the file either because the file is unable to be read or the user hasn't
        # added info for that site
        print(error)
        return None


def check_out_book(title: str, user: str) -> int:
    """
    Check out a book and update its status in the books.json file.

    :param title: The title of the book to be checked out.
    :param user: The name of the user checking out the book.
    :return: An integer code indicating the result of the operation.
        - 0: The book was successfully checked out and its status updated.
        - 1: The book is already checked out and cannot be checked out again.
        - 2: The JSON file containing book data was not found.

    """
    try:
        with open(file='./Data/books.json', mode='r') as data_file:
            data = json.load(data_file)  # Load the books.json data

        if data[title]["status"].find("checked out") != -1:
            # ASSERT: The book is checked out already
            return 1

        data[title]["status"] = f"checked out to {user}"  # Update the status of the provided book

        with open(file='./Data/books.json', mode='w') as data_file:
            json.dump(data, fp=data_file, indent=4)  # Overwrite books.json with updated info
        return 0

    except KeyError:
        return 2


def check_in_book(title: str) -> int:
    """
    Check in a book and update its status in the books.json file.

    :param title: The title of the book to be checked out.
    :param user: The name of the user checking in the book.
    :return: An integer code indicating the result of the operation.
        - 0: The book was successfully checked in and its status updated.
        - 1: The book is already checked in and cannot be checked out again.
        - 2: The JSON file containing book data was not found.

    """
    try:
        with open(file='./Data/books.json', mode='r') as data_file:
            data = json.load(data_file)  # Load the books.json data

        if data[title]["status"] == "checked in":
            # ASSERT: The book is checked out already
            return 1

        data[title]["status"] = f"checked in"  # Update the status of the provided book

        with open(file='./Data/books.json', mode='w') as data_file:
            json.dump(data, fp=data_file, indent=4)  # Overwrite books.json with updated info
        return 0

    except KeyError:
        return 2


def delete_book(title: str):
    try:
        with open(file='./Data/books.json', mode='r') as data_file:
            data = json.load(data_file)  # Load the books.json data

        if data[title]["status"] == "checked in":
            # ASSERT: The book is checked out already
            return 1

        with open(file='./Data/books.json', mode='w') as data_file:
            json.dump(data, fp=data_file, indent=4)  # Overwrite books.json with updated info
            return 0

    except KeyError:
        return 2
