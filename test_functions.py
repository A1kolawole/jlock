import pytest
from testfixtures import TempDirectory
from print_functions import *
from util_funcs import lock_depth_positive_check


def test_print_separation_line():
    assert print_separation_line('=', 2) == '\n\t==\n\n'
    assert print_separation_line('=', 0) == '\n\t\n\n'
    assert print_separation_line('=', 10) == '\n\t==========\n\n'
    assert print_separation_line('', 2) == '\n\t\n\n'
    assert print_separation_line('=', -1) == '\n\t\n\n'


extract_msg_file_content()
lock_depth_positive_check()