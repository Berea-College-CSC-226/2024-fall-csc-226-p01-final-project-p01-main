import random


def get_starting_balls():
    balls = int(input('how many balls would you like to start with (minimum 15 balls!): '))
    while balls < 15:
        balls = int(input('select at least 15 balls: '))
    return balls


def player_turn(balls):
    player_balls = int(input('how many balls would you like to pick up (maximum 4 balls: '))
    while player_balls < 1 or player_balls > 4:
        player_balls = int(input('pick up to 4 balls: '))
    while player_balls > balls:
        player_balls = int(input('pick no more than remaining balls: '))

    new_balls = balls - player_balls
    print('you picked ', player_balls)

    print('there are now', new_balls, 'balls ')
    return new_balls


def player_vs_player(balls):
    player1_name = input('player 1, what is your name?: ')
    player2_name = input('player 2, what is your name?: ')

    current_player = player1_name
    while balls > 0:
        print(f"{current_player}'s turn.")
        balls = player_turn(balls)
        if balls == 0:
            print(f"{current_player} wins!")
            break

        if current_player == player1_name:
            current_player = player2_name
        else:
            current_player = player1_name


def computer_turn(balls):
    computer_ball = random.randint(1, 4)
    while balls % 5 != 0 and (balls - computer_ball) % 5 != 0:  # when remaining balls is not a multiple of 5 and when
        computer_ball = random.randint(1, 4)  # computer is not picking to leave a multiple of 5
        # keep generating random picks until computer leaves a multiple of 5
    if computer_ball > balls:
        computer_ball = random.randint(1, balls)  # pick randomly up to # of remaining balls
    new_balls = balls - computer_ball

    print('computer picked', computer_ball)
    print(' there are now', new_balls, 'balls')
    return new_balls


def main():
    print("welcome to the game of nim!")
    print("players take 1-4 turn removing 1-4 balls. Who ever removes the last ball wins!")

    game_mode = input("Choose game mode (1 for player vs computer, 2 for player vs player): ")

    if game_mode == "1":
        balls = get_starting_balls()
        while balls >= 0:
            balls = player_turn(balls)
            if balls == 0:
                print('player  won')
                break

            balls = computer_turn(balls)
            if balls == 0:
                print('computer wins')
                break

    elif game_mode == "2":
        balls = get_starting_balls()
        player_vs_player(balls)
    else:
        print("Invalid game mode. Exiting.")
        return


if __name__ == "__main__":
    main()
