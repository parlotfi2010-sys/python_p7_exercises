#==================================
#==============Task 2==============
#==================================

import os

USER_FILE = 'user.txt'

def read_all_users() :
    """
    Read all users from the file.

    Returns
    -------
    list
        A list containing user information.
    """

    users = []

    try:
        with open(USER_FILE, 'r', encoding='utf-8') as file :
            for line in file :
                line = line.strip()

                if line == '' :
                    continue

                try:
                    user_id, name, email, status = line.split(',')

                    if status not in ['active', 'blocked'] :
                        print(f'Invalid status in this line : {line}')
                        continue

                    users.append([user_id, name, email, status])

                except ValueError :
                    print(f'Error reading this line: {line}')

    except FileNotFoundError :
        pass

    except OSError as error :
        print(f'Error opening file : {error}')
        return None

    return users


def save_users(users) :
    """
    Save all users to the file.

    Parameters
    ----------
    users : list
        A list containing user information.

    Returns
    -------
    bool
        True if saving is successful, otherwise False.
    """

    try:
        with open(USER_FILE, 'w', encoding='utf-8') as file :
            for user in users :
                file.write(f'{user[0]},{user[1]},{user[2]},{user[3]}\n')

        return True

    except OSError as error :
        print(f'Error saving file : {error}')
        return False


def valid_email(email) :
    """
    Check whether the email has a basic valid format.

    Parameters
    ----------
    email : str
        The email address to check.

    Returns
    -------
    bool
        True if the email format is valid, otherwise False.
    """

    if not isinstance(email, str) :
        return False

    if email.count('@') != 1 :
        return False

    if ' ' in email or ',' in email :
        return False

    username, domain = email.split('@')

    if username == '' or domain == '' :
        return False

    if '.' not in domain :
        return False

    if domain.startswith('.') or domain.endswith('.') :
        return False

    return True


def add_user(user_id, name, email, status) :
    """
    Add a new user to the file.

    Parameters
    ----------
    user_id : str or int
        The unique user ID.
    name : str
        The user's name.
    email : str
        The user's unique email address.
    status : str
        The user status: active or blocked.

    Returns
    -------
    None
    """

    user_id = str(user_id).strip()

    if not isinstance(name, str) :
        print('Error : Name must be a string.')
        return

    name = name.strip()

    if user_id == '' or not user_id.isdigit() :
        print('Error : ID must be a positive integer.')
        return

    if name == '' or ',' in name :
        print('Error : Invalid name.')
        return

    if not valid_email(email) :
        print('Error : Invalid email address.')
        return

    email = email.strip().lower()

    if not isinstance(status, str) :
        print('Error : Status must be a string.')
        return

    status = status.strip().lower()

    if status not in ['active', 'blocked'] :
        print('Error : Status must be active or blocked.')
        return

    users = read_all_users()

    if users is None :
        print('Error : Users could not be read.')
        return

    for user in users :
        if user[0] == user_id:
            print('Error : This ID already exists.')
            return

        if user[2].lower() == email :
            print('Error : This email already exists.')
            return

    users.append([user_id, name, email, status])

    if save_users(users) :
        print(f'User {name} has been successfully added.')


def find_user(search_value) :
    """
    Find a user by ID or name.

    Parameters
    ----------
    search_value : str or int
        The ID or name to search for.

    Returns
    -------
    list or None
        The matching user if found, otherwise None.
    """

    users = read_all_users()

    if users is None :
        return None

    search_value = str(search_value).strip()

    for user in users :
        if user[0] == search_value or user[1].lower() == search_value.lower() :
            print(
                f'ID : {user[0]}, Name: {user[1]}, '
                f'Email : {user[2]}, Status: {user[3]}'
            )
            return user

    print('User not found.')
    return None


def delete_user(user_id) :
    """
    Delete a user by ID and save the change to the file.

    Parameters
    ----------
    user_id : str or int
        The ID of the user to delete.

    Returns
    -------
    None
    """

    user_id = str(user_id).strip()

    users = read_all_users()

    if users is None :
        print('Error : Users could not be read.')
        return

    for user in users :
        if user[0] == user_id :
            users.remove(user)

            if save_users(users) :
                print(f'User {user_id} has been deleted.')

            return

    print('User not found.')


def update_user(user_id, email=None, status=None) :
    """
    Update a user's email or status.

    Parameters
    ----------
    user_id : str or int
        The ID of the user to update.
    email : str or None
        The new email address.
    status : str or None
        The new status.

    Returns
    -------
    None
    """

    user_id = str(user_id).strip()

    users = read_all_users()

    if users is None:
        print('Error: Users could not be read.')
        return

    target_user = None

    for user in users :
        if user[0] == user_id :
            target_user = user
            break

    if target_user is None :
        print('User not found.')
        return

    if email is None and status is None :
        print('Error : No changes were provided.')
        return

    if email is not None :
        if not valid_email(email) :
            print('Error : Invalid email address.')
            return

        email = email.strip().lower()

        for user in users :
            if user[0] != user_id and user[2].lower() == email :
                print('Error : This email already exists.')
                return

        target_user[2] = email

    if status is not None :
        if not isinstance(status, str) :
            print('Error : Status must be a string.')
            return

        status = status.strip().lower()

        if status not in ['active', 'blocked'] :
            print('Error : Status must be active or blocked.')
            return

        target_user[3] = status

    if save_users(users):
        print(f'User {user_id} has been updated.')


def list_user():
    """
    Display all users stored in the file.

    Returns
    -------
    None
    """

    users = read_all_users()

    if users is None :
        print('Error : Users could not be read.')
        return

    if len(users) == 0 :
        print('No users have been recorded yet.')
        return

    print('\nUsers list :')

    for user in users :
        print(
            f'ID : {user[0]}, Name: {user[1]}, '
            f'Email : {user[2]}, Status: {user[3]}'
        )


def generate_report() :
    """
    Display the total number of users and their statuses.

    Returns
    -------
    None
    """

    users = read_all_users()

    if users is None :
        print('Error : Users could not be read.')
        return

    active_count = 0
    blocked_count = 0

    for user in users :
        if user[3] == 'active' :
            active_count += 1

        elif user[3] == 'blocked' :
            blocked_count += 1

    total_users = len(users)

    print('\nUsers report :')
    print(f'Total users : {total_users}')
    print(f'Active users : {active_count}')
    print(f'Blocked users : {blocked_count}')


def run_tests() :
    """
    Test normal and invalid inputs using a separate test file.

    Returns
    -------
    None
    """

    global USER_FILE

    original_file = USER_FILE
    test_file = 'test_user.txt'

    try:
        USER_FILE = test_file

        if os.path.exists(test_file):
            os.remove(test_file)

        print('\nTesting valid user entries : ')
        add_user(1, 'Ali', 'ali@gmail.com', 'active')
        add_user(2, 'Sara', 'sara@gmail.com', 'blocked')

        print('\nTesting duplicate ID : ')
        add_user(1, 'Reza', 'reza@gmail.com', 'active')

        print('\nTesting invalid email : ')
        add_user(3, 'Reza', 'reza.gmail.com', 'active')

        print('\nTesting invalid status : ')
        add_user(3, 'Reza', 'reza@gmail.com', 'pending')

        print('\nTesting duplicate email : ')
        add_user(3, 'Reza', 'ali@gmail.com', 'active')

        print('\nTesting user listing : ')
        list_user()

        print('\nTesting report : ')
        generate_report()

    finally :
        USER_FILE = original_file

        try :
            if os.path.exists(test_file) :
                os.remove(test_file)
        except OSError as error :
            print(f'Error removing test file : {error}')


def main() :
    """
    Display the menu and run the user management program.

    Returns
    -------
    None
    """

    while True :
        print('\n===== User Management System =====')
        print('1. Add user')
        print('2. Find user')
        print('3. Delete user')
        print('4. Update user')
        print('5. List all users')
        print('6. Generate report')
        print('7. Run tests')
        print('8. Exit')

        choice = input('Choose an option : ').strip()

        if choice == '1' :
            user_id = input('Enter user ID : ')
            name = input('Enter user name : ')
            email = input('Enter user email : ')
            status = input('Enter status (active/blocked) : ')

            add_user(user_id, name, email, status)

        elif choice == '2' :
            search_value = input('Enter user ID or name : ')
            find_user(search_value)

        elif choice == '3' :
            user_id = input('Enter user ID to delete : ')
            delete_user(user_id)

        elif choice == '4' :
            user_id = input('Enter user ID to update : ')

            print('1. Update email')
            print('2. Update status')
            print('3. Update both')

            update_choice = input('Choose an option: ').strip()

            if update_choice == '1' :
                email = input('Enter new email : ')
                update_user(user_id, email=email)

            elif update_choice == '2' :
                status = input('Enter new status : ')
                update_user(user_id, status=status)

            elif update_choice == '3' :
                email = input('Enter new email : ')
                status = input('Enter new status : ')
                update_user(user_id, email=email, status=status)

            else:
                print('Invalid update option.')

        elif choice == '5' :
            list_user()

        elif choice == '6' :
            generate_report()

        elif choice == '7' :
            run_tests()

        elif choice == '8' :
            print('Program closed.')
            break

        else :
            print('Invalid menu option. Please try again.')


if __name__ == '__main__':
    main()
