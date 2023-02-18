import os
import print_functions
import lock_functions
import unlock_functions
import util_funcs


def help_command():
    ''' Call all the command help print functions.'''

    separation_str = '=' * 50
    print(f'\n\t{separation_str}\n')
    print_functions.print_help_welcome()
    print(f'\n\t{separation_str}\n')
    print_functions.print_lock_help()
    print(f'\n\t{separation_str}\n')
    print_functions.print_unlock_help()
    print(f'\n\t{separation_str}\n')
    print_functions.print_msg_help()
    print(f'\n\t{separation_str}\n')
    print_functions.print_locked_help()
    print(f'\n\t{separation_str}\n')
    print_functions.print_clear_help()
    print(f'\n\t{separation_str}\n')

def msg_command():
    # displays list of decrypted plain text message files
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]
    if len(decrypted_file_list) == 0:
        print('\n\tNo plaintext message files available.\n')
    else:
        print('\n\tPlaintext message files:\n')
        for file_name in decrypted_file_list:
            print_functions.print_msg_file_info()


def locked_command():
    # displays list of encrypted (locked) files
    encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
    if len(encrypted_file_list) == 0:
        print('\n\tNo encrypted message files available.\n')
    else:
        print('\n\tEncrypted message files:\n')
        for file_name in encrypted_file_list:
            print_functions.print_locked_file_info()


def clear_command():
    # gather all text files from current directory (use list comprehension)
    lock_file_list = [file for file in os.listdir() if file.endswith('_lock.txt')]
    key_file_list = [file for file in os.listdir() if file.endswith('_key.txt')]
    encrypted_file_list = [file for file in os.listdir() if file.endswith('_encrypted_msg.txt')]
    decrypted_file_list = [file for file in os.listdir() if file.endswith('_decrypted_msg.txt')]

    # assemble ALL text file list
    master_text_file_list = lock_file_list + key_file_list + encrypted_file_list + decrypted_file_list
    # print(master_text_file_list)
    for text_file in master_text_file_list:
        os.remove(text_file)

    print('\n\n\tAll \'lock\', \'key\', \'encrypted message\', and \'decrypted message\' text files removed.\n')


def unlock_command(arg_list: list):
    target_encrypted_file: str = arg_list[2]
    file_list = os.listdir()
    if (target_encrypted_file in file_list) and (len(target_encrypted_file) == 22) and \
            (target_encrypted_file[-18:] == '_encrypted_msg.txt'):
        unlock_functions.unlock(target_encrypted_file)
    else:
        print(f'\n\t{target_encrypted_file} does not exist or is invalid\n')


def lock_command(arg_list: list):
    # check if an int is passed as the lock depth
    util_funcs.validate_lock_depth()
    # check if lock depth is greater than zero
    util_funcs.lock_depth_positive_check()

    lock_file = util_funcs.generate_lock_file(arg_list[2])
    lock_functions.lock(arg_list[3], lock_file)