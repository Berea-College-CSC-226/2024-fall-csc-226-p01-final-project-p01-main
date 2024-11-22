from inspect import getframeinfo, stack
from Game_of_Nim import player_turn
from Game_of_Nim import computer_turn
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


def player_turn_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the is_i_steal_pennies() function.

    :return: None
    """
    print("\nRunning pennies_testsuite()).")

    # Remember that i_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    unittest(player_turn(10) == 6)  # because three quarters, 1 dime, and 3 pennies equals 88 cents
    unittest(player_turn(6) == 2)
    unittest(player_turn(5) == 3)

    print("Run of pennies_testsuite() complete.")

def computer_turn_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the is_i_steal_pennies() function.

    :return: None
    """
    print("\nRunning computer_turn_testsuites()).")

    # Remember that i_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    unittest(computer_turn(10) == 6)  # because three quarters, 1 dime, and 3 pennies equals 88 cents
    unittest(computer_turn(7) == 2)
    unittest(computer_turn(2) == 3)

    print("Run of computer_turn() complete.")



def main():
    """
    This main function is intended to test the correctness of the i_steal_pennies() function

    :return:
    """

    player_turn_testsuite()
    computer_turn_testsuite()


if __name__ == "__main__":
    # If you run this code directly (i.e., hit the green run button on this file), it runs the test suite
    # If you call this code from another file (e.g., t05_making_change_interactive.py), it will NOT run the test suite
    main()
