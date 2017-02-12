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
    def __init__(self, user_input, user_file, user_dir, user_path, path_type):
        self.user_input = user_input
        self.user_file  = user_file
        self.user_dir   = user_dir
        # self.user_path  = user_path
        # self.path_type  = path_type

    def get_path(self, user_file, user_dir, user_input):
        # Number of attempts before program exits, due to invalid input.
        tries = 3

        user_input = input("Please provide the path to a file or directory that you wish to be deleted." + '\n')

        # If it is a file or directory it will call the appropriate method to delete file.
        if UserInput.file_or_dir(self, user_input):
            if os.path.isfile(UserInput.get_file(user_input)):
                File.delete_file(user_input)
            else:
                Directory.delete_file(user_input)
        # User input validation. Will exit if user fails to input valid path after 3 tries.
        else:
            while tries > 0:
                if os.path.isfile(user_input):
                    print("Congratulations, you've provided a valid file path")
                    break
                elif os.path.exists(user_input) and os.path.isdir:
                    print("Congratulations, you've provided a valid directory")
                    break
                if not os.path.exists(user_input):
                    print(user_input + ' is not a valid file path. Try again.')
                else:
                    print('There\'s {0} attempt(s) remaining.'.format(tries))
                    break

                user_input = input('Please provide the path to a file or directory that you wish to be deleted.' + '\n')

                if os.path.isfile(user_input):
                    print('Congratulations, you\'ve provided a valid file path')
                elif os.path.exists(user_input) and os.path.isdir:
                    print('Congratulations, you\'ve provided a valid directory')
                else:
                    print(user_input + ' is not a valid file path.')
                    print('Exiting...')

    # Inform user of path type, then set to appropriate path type.
    def file_or_dir(self, user_input, user_path):
        if not os.path.exists(user_input):
            print(user_input + ' is not a valid file path.')
            return False
        elif os.path.isfile(user_path):
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
        # The number of attempts before the program exits, for invalid input.
        tries = 3
        # Input(file/directory) validation.
        user_input = input("Please provide the path to a file or directory that you wish to be deleted." + '\n')

        if os.path.isfile(user_input):
            print("You've provided a valid file path. Are you sure you'd like to delete this? (Y/n)")

        elif os.path.exists(user_input) and os.path.isdir:
            print("Congratulations, you've provided a valid directory")

        elif not os.path.exists(user_input):
            while tries > 0:
                tries -= 1
                if os.path.isfile(user_input):
                    print("Congratulations, you've provided a valid file path")
                    break
                elif os.path.exists(userInput) and os.path.isdir:
                    print("Congratulations, you've provided a valid directory")
                    break
                if tries != 0:
                    print(userInput + " is not a valid file path. Try again.")
                else:
                    print("There are {0} attempts remaining.".format(tries))
                    break
                if tries == 1:
                    print("There is {0} attempt remaining.".format(tries))
                elif tries == 0:
                    print("There are no attempt remaining.")
                userInput = input("Please provide the path to a file or directory that you wish to be deleted." + '\n')
            if os.path.isfile(user_input):
                print("Congratulations, you've provided a valid file path")
            elif os.path.exists(user_input) and os.path.isdir:
                print("Congratulations, you've provided a valid directory")

        else:
            print(user_input + " is not a valid file path.")
            print("Exiting...")


class Directory(object):
    """ A directory object has the following properties:

    Attributes:
        name: The name of the directory, without the directory path.
        contents: A list of what is contained in the directory.
    """
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    # def delete_dir(self):
    #     # The number of attempts before the program exits, for invalid input.
    #     tries = 3
    #     # Input(file/directory) validation.
    #     userInput = input("Please provide the path to a file or directory that you wish to be deleted." + '\n')
    #
    #     if os.path.isfile(userInput):
    #         print("You've provided a valid file path. Are you sure you'd like to delete this? (Y/n)")
    #
    #     elif os.path.exists(userInput) and os.path.isdir:
    #         print("Congratulations, you've provided a valid directory")
    #
    #     elif not os.path.exists(userInput):
    #         while tries > 0:
    #             tries -= 1
    #             if os.path.isfile(userInput):
    #                 print("Congratulations, you've provided a valid file path")
    #                 break
    #             elif os.path.exists(userInput) and os.path.isdir:
    #                 print("Congratulations, you've provided a valid directory")
    #                 break
    #             if tries != 0:
    #                 print(userInput + " is not a valid file path. Try again.")
    #             else:
    #                 print("There are {0} attempts remaining.".format(tries))
    #                 break
    #             if tries == 1:
    #                 print("There is {0} attempt remaining.".format(tries))
    #             elif tries == 0:
    #                 print("There are no attempt remaining.")
    #             userInput = input(
    #                 "Please provide the path to a file or directory that you wish to be deleted." + '\n')
    #         if os.path.isfile(userInput):
    #             print("Congratulations, you've provided a valid file path")
    #         elif os.path.exists(userInput) and os.path.isdir:
    #             print("Congratulations, you've provided a valid directory")
    #
    #     else:
    #         print(userInput + " is not a valid file path.")
    #         print("Exiting...")