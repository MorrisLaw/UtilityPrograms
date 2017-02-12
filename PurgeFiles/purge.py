# === Purpose:
# Given a file path/directory, delete it. If it's a folder, remove its folders and files including the folder itself.
#
# === File:
# purge.py
#
# === Author:
# Jeremy Morris
import os
import sys


class UserInput(object):
    """ A UserInput object has the following properties:

        Attributes:
            user_input: This is what the user provides in the form of either a file or directory path.
            tries: The number of attempts to get a valid path before the program exits.
            user_path: The valid file path given by the user.
    """
    user_input = ''
    tries = 0
    user_path = ''

    def __init__(self, user_input, tries, user_path):
        self.user_input = user_input
        self.tries = tries
        self.userPath = ''

    def get_path(self):
        # Number of attempts before program exits, due to invalid input.
        tries = 3
        user_input = input('Please provide a file or directory that you\'d like deleted.' + '\n')
        # Attempt to get a valid path until attempts reach the trie(attempt) limit.
        while tries > -1:
            if tries == -1:
                print('You\'ve failed to provide a valid file path. Exiting the program...')
                break
            if os.path.exists(user_input) and os.path.isfile(user_input):
                print('You\'ve provided a valid file path...')
                break
            elif os.path.exists(user_input) and os.path.isdir:
                print('You\'ve provided a valid directory...')
                break
            elif not os.path.exists(user_input) and tries == 0:
                print(user_input + ' is not a valid file path.' + '\n'
                      + 'You\'ve failed to provide a valid file path.'
                      + 'Exiting the program...')
                user_input = ''
                break
            elif not os.path.exists(user_input):
                user_input = input(user_input + ' is not a valid file path. Please try again.'
                                   + '\n' + 'You have {0} attempt(s) remaining.'.format(tries) + '\n')
                tries -= 1

        UserInput.set_user_path(self, user_input)
        return user_input

    def set_user_path(self, user_path):
        self.user_path = user_path

    def get_user_path(self, user_path):
        return self.user_path


class File(object):
    """ A file object has the following properties:

    Attributes:
        name: The name of the file without the directory path.
        type: The file type, providedby parsing the extension.
    """
    # name = ''
    # type = ''
    decision = ''
    user_path = ''

    def __init__(self, name, type, decision, user_path):
        # self.name = name
        # self.type = type
        self.decision = decision
        self.user_path = user_path

    def delete_file(self, user_path):
        # Verify the deletion, by asking the user if they're sure.
        decision = input('\n' + 'Would you like to delete this file ? (Y/n)' + '\n')
        # If yes, ask again twice. Just to be sure.
        if decision == 'y' or decision == 'yes' or decision == 'Y' or decision == 'YES':
            decision = input('Are you sure you want to delete this file and all of it\'s contents ? (Y/n)' + '\n')
            if decision == 'y' or decision == 'yes' or decision == 'Y' or decision == 'YES':
                decision = input('It\'s not coming back... (Fine with me/ NO, DON\'T DO IT)' + '\n')
                if decision == 'y' or decision == 'yes' or decision == 'Y' or decision == 'YES' or decision == 'Fine ' \
                                                                                                               'with ' \
                                                                                                               'me':
                    # Obliterates the file.
                    os.remove(UserInput.get_user_path(self, user_path))
                    print('This file is now gone!')
                else:
                    print('Exiting program, your file is safe...')
                    sys.exit(None)
            else:
                print('Exiting program, your file is safe...')
                sys.exit(None)
        else:
            print('Exiting program, your file is safe...')
            sys.exit(None)

    @property
    def set_file_name(self, name, user_path):
        self.name = os.path.basename(UserInput.get_user_path(self, name, user_path))

    def get_file_name(self, name):
        return self.name


class Directory(object):
    """ A directory object has the following properties:

    Attributes:
        name: The name of the directory, without the directory path.
        contents: A list of what is contained in the directory.
        decision: The decision as to whether or not the given path will be deleted.
        path_value: The full file path of the user_input.
    """
    # name = ''
    # contents = []
    decision = ''
    user_path = ''

    def __init__(self, name, contents, decision, user_path):
        # self.name = name
        # self.contents = contents
        self.decision = decision
        self.user_path = user_path

    def delete_dir(self, user_path):
        # Verify the deletion, by asking the user if they're sure.
        decision = input('\n' + 'Would you like to delete this directory ? (Y/n)' + '\n')
        # If yes, ask again twice. Just to be sure.
        if decision == 'y' or decision == 'yes' or decision == 'Y' or decision == 'YES':
            decision = input('Are you sure you want to delete this directory and all of it\'s contents ? (Y/n)' + '\n')
            if decision == 'y' or decision == 'yes' or decision == 'Y' or decision == 'YES':
                decision = input('It\'s not coming back... (Fine with me/ NO, DON\'T DO IT)' + '\n')
                if decision == 'y' or decision == 'yes' or decision == 'Y' or decision == 'YES' or decision == 'Fine ' \
                                                                                                               'with ' \
                                                                                                               'me':
                    # Obliterates the directory.
                    os.rmdir(os.path.realpath(UserInput.get_user_path(self, user_path)))
                    print('This Directory and all of it\'s contents are now gone!')
                else:
                    print('Exiting program, your directory is safe...')
                    sys.exit(None)
            else:
                print('Exiting program, your directory is safe...')
                sys.exit(None)
        else:
            print('Exiting program, your directory is safe...')
            sys.exit(None)


# Instance of UserInput object.
ui = UserInput
ui_path_value = ui.get_path(ui)
if ui_path_value != '':
    if os.path.isfile(ui_path_value):
        File.delete_file(ui, ui_path_value)
    else:
        Directory.delete_dir(ui, ui_path_value)