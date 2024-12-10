######################################################################
# Author: Kirsten Fuson
# Username: fusonk
#
# Assignment: Final Project
#
# Purpose: This program is designed to test my final project
#
#
######################################################################
# Acknowledgements:
#   Original test code: Scott Hegan
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from inspect import getframeinfo, stack
from game_run import Game

def unittest(self, did_pass):
    """
    Prints the result of a test
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

    self.game = Game()

    def test_monster():
        """
        Test if monster takes damage correctly
        :return:
        """
        monster = self.game.monster()
        monster.take_damage(1)

        #Currently monster is taking too much damage at one time

