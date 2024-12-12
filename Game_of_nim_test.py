######################################################################
# Author: DieuMerci Nshizirungu
# Username: nshizirungud
#
#
#
# Purpose: Test suite for the game of nim
#
#
#
######################################################################
# Acknowledgements: Gagan Phuyal, Bishal, T05 take a penny leave a penny
#
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from inspect import getframeinfo, stack
from Game_of_Nim import GameOfNim

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

def game_of_nim_testsuite():
    """
    The test suite function runs unit tests for Game of Nim logic.

    :return: None
    """
    print("\nRunning game_of_nim_testsuite().")

    # Initialize game instance
    game = GameOfNim()

    # Test initial state
    unittest(game.balls == 15)
    unittest(game.current_player == "Player 1")

    # Test setting starting balls
    game.balls = 20
    unittest(game.balls == 20)

    # Test player turn logic
    game.balls = 10
    player_input = 3  # player removing 3 balls
    game.balls -= player_input
    unittest(game.balls == 7)

    # Test computer turn logic
    game.balls = 7
    computer_input = 2  # computer taking out 2 balls
    game.balls -= computer_input
    unittest(game.balls == 5)

    # Test game over condition
    game.balls = 1
    player_input = 1  # Simulate removing the last ball
    game.balls -= player_input
    unittest(game.balls == 0)

if __name__ == "__main__":
    game_of_nim_testsuite()