"""
# Title: main driver for a simple social network project
# Who: ALarson
# What/When: 4/24/2022 - started assignment
"""
import csv
import user_status
import users



def init_user_collection():
    """
    Creates and returns a new instance of UserCollection
    """
    user = users.UserCollection()
    return user


def init_status_collection():
    """
    Creates and returns a new instance of UserStatusCollection
    """
    status = user_status.UserStatusCollection()
    return status


def load_users(filename, user_collection):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    """
    try:
        with open(filename, newline='', encoding="UTF-8") as file:
            user_collection.database = csv.DictReader(file)
    except FileNotFoundError:
        print('File not found')


def save_users(filename, user_collection):
    """
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    """
    header = ['USER_ID', 'EMAIL', 'NAME', 'LASTNAME']
    try:
        with open(filename, mode='a', newline='', encoding="UTF-8") as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=header)
            for key, values in user_collection().database:
                row = {key: values}
                writer.writerow(row)
                return True
    except FileNotFoundError:
        print('File not found')
        return False


def load_status_updates(filename, status_collection):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    """


def save_status_updates(filename, status_collection):
    """
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    """


def add_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    """
    new_user = user_collection.add_user(user_id, email, user_name, user_last_name)
    return new_user


def update_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there are any errors.
    - Otherwise, it returns True.
    """
    updated_user = user_collection.modify_user(user_id, email, user_name, user_last_name)
    return updated_user


def delete_user(user_id, user_collection):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    del_user = user_collection.delete_user(user_id)
    return del_user


def search_user(user_id, user_collection):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    """
    find_user = user_collection.search_user(user_id)
    return find_user


def add_status(status_id, user_id, status_text, status_collection):
    """
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    add_new_status = status_collection.add_status(status_id, user_id, status_text)
    return add_new_status


def update_status(status_id, user_id, status_text, status_collection):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    updated_status = status_collection.modify_status(status_id, user_id, status_text)
    return updated_status


def delete_status(status_id, status_collection):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    del_status = status_collection.delete_status(status_id)
    return del_status


def search_status(status_id, status_collection):
    """
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    find_status = status_collection.search_status(status_id)
    return find_status
