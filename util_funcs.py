import random
import string
import sys
import os


def generate_lock_file(size):
    # generate random lock file name: [random]_lock.txt
    lock_file_name = generate_unique_lock_file_name()
    try:
        return write_to_lock_file(lock_file_name, size)

    except Exception as file_error:
        print(f'\n\tAn error occurred while trying to write to {lock_file_name}:'
              f'{file_error}\n')

    return None


def generate_unique_lock_file_name():
    # generate random lock file name: [random]_lock.txt
    files_in_dir = os.listdir()
    timeout_limit = None
    while timeout_limit < 10:
        random_file_name = '_lock.txt'
        for _ in range(8):
            random_letter = random.choice(string.ascii_letters)
            random_file_name = random_letter + random_file_name
        if random_file_name not in files_in_dir:
            break
        else:
            timeout_limit += 1

    return random_file_name


def write_lock_values_to_file(size, text_file):
    # writes the values to a file
    for line_ct in range(int(size)):
        rand_int1 = random.randint(0, sys.maxsize)
        if line_ct < int(size) - 1:
            print(f'{rand_int1}', file=text_file)
            continue
        text_file.write(f'{rand_int1}')


def write_to_lock_file(file_name, size_val):
    with open(file_name, 'w') as file_name:
        write_lock_values_to_file(size_val, generate_unique_lock_file_name())
    return file_name


def lock_depth_positive_check(depth, arg_val):
    if depth <= 0:
        print(f'\n\tInvalid lock depth: \'{arg_val}\'. Must be an integer greater than 0(zero).\n')
        return None
    return depth


def validate_lock_depth(arg_value: str):
    # check if an int is passed as the lock depth
    try:
        lock_depth = int(arg_value)
        return lock_depth_positive_check(lock_depth, arg_value)

    except ValueError:
        print(f'\n\tInvalid lock depth: \'{arg_value}\'. Must be an integer greater than 0(zero).\n')
        return None