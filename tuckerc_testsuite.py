######################################################################
# Author: Caleb Tucker
# Username: tuckerc
#
# P01: Final Project
#
# Purpose: To create an interactive calendar
#######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from tuckerc_final import *
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


def final_test_suite():
    """
    """

    unittest(fillerfunction("BeamMeUp") == "Scottie")


final_test_suite()
