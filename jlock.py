import sys
import util_funcs
import os
import json
from lock_functions import lock
from unlock_functions import unlock
import print_functions
import command_functions


def jlock_main():
    # get command line arguments
    arg_list = sys.argv
    arg_list_len = len(arg_list)

    # check for empty string in command line args - empty strings are invalid input
    if '' in arg_list:
        print('Error: invalid command')
        return

    parse_command_line_args(arg_list)



def parse_command_line_args(arg_list: list):
    arg_list_len = len(arg_list)

    if arg_list_len == 1:
        print_functions.print_welcome_message()

    elif arg_list_len == 2:
        command = arg_list[1]
        if command == '-help' or command == '-h':
            command_functions.help_command()

        elif command == '-msg':
            # displays list of decrypted plain text message files
            command_functions.msg_command()

        elif command == '-locked':
        # displays list of encrypted (locked) files
            command_functions.locked_command()

        elif command == '-clear':
            # gather all text files from current directory (use list comprehension)
            command_functions.clear_command()
        else:
            print('Error: invalid command')

    elif arg_list_len == 3:
        if arg_list[1] == '-unlock':
            command_functions.unlock_command()
        else:
            print('Error: invalid command')


    elif arg_list_len == 4:
        if arg_list[1] == '-lock':
           command_functions.lock_command()
        else:
            print('Error: invalid command')

    else:
        print('Error: invalid command')


if __name__ == '__main__':
    jlock_main()
