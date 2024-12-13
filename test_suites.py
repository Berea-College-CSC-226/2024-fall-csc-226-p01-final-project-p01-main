from StarFLARE import Game, Player, Dodgeball
from inspect import getframeinfo, stack
import pygame

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

def test_player_movemnt():
    """
    this test the player's movement and to see if it stays within the boundary
    """
    player = Player(500, 500) #the set boundary

    #this is for the left key
    player.rect.x = 250 #sets the player in the middle of the screen
    pygame.key.get_pressed([True, False])
    player.left_right()
    unittest(player.rect.x == 245) #checks if the player moved over 5 spaces to the left

    # this is for the right key
    player.rect.x = 250  # sets the player in the middle of the screen
    pygame.key.get_pressed([True, False])
    player.left_right()
    unittest(player.rect.x == 265) #checks to see if the player moved over 10 spaces to the right



def test_dodgeball():
    """
    this test if new dodgeballs are created at the top of the screen randomly
    """
    ball = Dodgeball()
    unittest(0 <= ball.rect.x <= 500 - ball.rect.width)  # the balls should only spawn within the screen's boundary
    unittest(0 <= ball.rect.y <= 0)  # the balls should spawn randomly at the top


def test_ball_movement():
    """
    this test the dodgeball's movement and to see if it stays within the boundary
    """
    ball = Dodgeball()
    start_position = ball.rect.y #Stores the current y position of the ball.
    ball.move_down()  # calls the move_down function
    unittest(ball.rect.y == start_position + ball.speed)  # checks if the y postion has changed by the speed


def test_collision():
    """
    This checks the collision between the falling dodgeballs and the player
    """
    game = Game()
    player = game.player #gets the player from the game
    ball = Dodgeball()


if __name__ == "__main__":
    unittest()
    test_player_movemnt()
    test_dodgeball()
    test_ball_movement()
    test_collision()





