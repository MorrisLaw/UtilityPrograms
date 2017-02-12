# === Purpose:
# Given a file path/directory, delete it. If it's a folder, remove its folders and files including the folder itself.
#
# === File:
# purge.py
#
# === Author:
# Jeremy Morris
import os


class UserInput(object):
    """ A UserInput object has the following properties:

        Attributes:
            user_input: This is what the user provides in the form of either a file or directory path.
    """

    def __init__(self, user_input, user_file, user_dir, user_path, path_type, tries):
        self.user_input = user_input
        self.user_file = user_file
        self.user_dir = user_dir
        self.tries = tries
        # self.user_path  = user_path
        # self.path_type  = path_type

    def get_path(self):
        # Number of attempts before program exits, due to invalid input.
        tries = 3
        user_input = input('Please provide a file or directory that you\'d like deleted.' + '\n')

        while tries > -1:
            if tries == -1:
                print('You\'ve failed to provide a valid file path. Exiting the program...')
                break
            if os.path.exists(user_input) and os.path.isfile(user_input):
                print('You\'ve provided a valid file path')
                print('Exiting...')
                break
            elif os.path.exists(user_input) and os.path.isdir:
                print('You\'ve provided a valid directory')
                print('Exiting...')
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

        return user_input

    # Inform user of path type, then set to appropriate path type.
    def file_or_dir(self, user_input):
        if not os.path.exists(user_input):
            return False
        elif os.path.isfile(user_input):
            print('You\'ve provided a valid file path')
            UserInput.set_file(self, user_input)
            return True
        else:
            print('You\'ve provided a valid directory')
            UserInput.set_dir(self, user_input)
            return True

    def set_file(self, user_file, user_input):
        self.user_file = user_input

    def get_file(self, user_file):
        return user_file

    def set_dir(self, user_dir, user_input):
        self.user_dir = user_input

    def get_dir(self, user_dir):
        return user_dir

    # @property
    # def path_type(self, user_path, user_file, user_dir):
    #     if os.path.isfile(UserInput.file_or_dir()):
    #         self.user_path = user_file
    #     else:
    #         self.user_path = user_dir

class File(object):
    """ A file object has the following properties:

    Attributes:
        name: The name of the file without the directory path.
        type: The file type, providedby parsing the extension.
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def delete_file(self):
        print('File YAY')


class Directory(object):
    """ A directory object has the following properties:

    Attributes:
        name: The name of the directory, without the directory path.
        contents: A list of what is contained in the directory.
    """
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def delete_dir(self):
        print('Directory YAY')


ui = UserInput
ui.get_path(ui)