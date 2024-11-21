from project import *
import sys

from inspect import getframeinfo, stack

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def final_project_test_suite():
    """
    A test suite for testing ????????
    """

    pass
    #to do: add tests



final_project_test_suite()
