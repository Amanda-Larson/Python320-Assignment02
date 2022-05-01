"""
Classes for user information for the social network project
"""
# pylint: disable=R0903

from loguru import logger

logger.info("Let's get to debugging users.py")
logger.add("users_and_status.log", backtrace=True, diagnose=True)


class Users:
    """
    Contains user information
    """

    def __init__(self, user_id, email, user_name, user_last_name):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name
        logger.info("User class instantiated")


class UserCollection():
    """
    Contains a collection of Users objects
    """

    def __init__(self):
        logger.info("User Collection instantiated.")
        self.database = {}


    def add_user(self, user_id, email, user_name, user_last_name):
        """
        Adds a new user to the collection
        """
        if user_id in self.database:
            logger.info("Reject new status  -  status_id already exists")
            return False
        new_user = Users(user_id, email, user_name, user_last_name)
        self.database[user_id] = new_user
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        """
        Modifies an existing user
        """
        if user_id not in self.database:
            logger.info(f'{user_id} not in the database')
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        return True

    def delete_user(self, user_id):
        """
        Deletes an existing user
        """
        if user_id not in self.database:
            logger.info(f'{user_id} not in the database')
            return False
        del self.database[user_id]
        return True

    def search_user(self, user_id):
        """
        Searches for user data
        """
        if user_id not in self.database:
            logger.info(f'{user_id} not in the database')
            return Users(None, None, None, None)
        return self.database[user_id]
