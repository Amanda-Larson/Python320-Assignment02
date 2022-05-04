# Errors fixed

# Testing menu.py using Pysnooper/Logger
1. ~~Load the users database.~~
2. ~~Add a new user and confirm you get a success message.~~
    - add_user failed because there was no return, added in main.py and ran successfully
3. ~~Try to add the same user ID again and confirm you get an error message.~~
4. ~~Update the name of an existing user.~~
    - update_user ran from menu.py got a TypeError...was missing user_collection parameter, added in
5. ~~Try to update the name of a non-existing user and confirm you get an error message.~~
6. ~~Search for an existing user and return that user's email, name and last name.~~
    - triggered AttributeError: no variable "name" , changed name to "user_id" and ran successfully
7. ~~Search for a non-existing user and return a message indicating that the user does not exist.~~
    - functions properly
8. ~~Delete an existing user.~~
    - functions properly
9. ~~Try to delete a non-existing user and confirm you get an error message.~~
    - functions properly - no debugging required
10. Save the users' database.
11. ~~Load the status database.~~
12. ~~Add a new status and confirm you get a success message.~~
    - functions properly - no debugging required
13. ~~Try to add the same status ID again and confirm you get an error message.~~
    - functions properly - no debugging required
14. ~~Update the text of an existing status ID.~~
    - Unexpected function behavior - received wrong statement from if-statement. Used pysnooper to investigate and change the method being called from add_status to update_status.
15. ~~Try to update the text of a non-existing status ID and confirm you get an error message.~~
    - functions properly - no debugging required
16. ~~Search for an existing status ID and return the ID of the user that created the status and the status text.~~
    - Solution: line 144 in function changed to result.status_id
    - Issue 2: Parameters were not in the correct order
    - Solution: PySnooper(depth=3) to walk through code and
17. ~~Search for a non-existing status ID and return a message indicating that the status ID does not exist.~~
    - functions properly after fixing 16
18. ~~Delete an existing status.~~
    - functions properly
19. ~~Try to delete a non-existing status and confirm you get an error message.~~
    - functions properly
20. Save the status database.
21. ~~Make sure menu options are case-insensitive (i.e., typing "a" or "A" works in the same way).~~
    - In line 199, key error issue stemming from missing .upper() method on user input 