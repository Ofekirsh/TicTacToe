import random


def explain():
    """
    explain the game for the user
    :return:
    """
    clean_gread = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Hello, the name of the game TicTacToe\nThis is the grid")
    print_grid(clean_gread)
    print("If you want to choose position that's the positions")


def is_winning(board, mark):
    """
    check if there is winner in the game
    :param board: board status
    :param mark: ?
    :return: True / Flase
    """
    if ((board[7] == board[8] == board[9] == mark.upper()) or
            (board[4] == board[5] == board[6] == mark.upper()) or
            (board[1] == board[2] == board[3] == mark.upper()) or
            (board[7] == board[4] == board[1] == mark.upper()) or
            (board[8] == board[5] == board[2] == mark.upper()) or
            (board[7] == board[5] == board[3] == mark.upper()) or
            (board[9] == board[5] == board[1] == mark.upper()) or
            (board[9] == board[6] == board[3] == mark.upper())):
        return True


def mark_input(marker, position, board):
    """
    mark input on borad
    :param marker: the sign to mark
    :param position: the position to mark
    :param board: the borad to mark on
    :return: None
    """
    if marker.upper() == 'X':
        board[position] = 'X'
    elif marker.upper() == 'O':
        board[position] = 'O'


def random_first_player():
    """
    random the first player to play
    :return: 1/2
    """
    var = random.randrange(1, 3)
    if var == 1:
        print('PLAYER 1, LETS GO')
    if var == 2:
        print('PLAYER 2, LETS GO')
    return var


def determine_player_1_sign():
    """
    function to determine player 1 sign
    :return: player 1 sign
    """
    player_1_sign = ''
    while (player_1_sign.upper() != 'X') or (player_1_sign.upper() != 'O'):
        player_1_sign = input("HI PLAYER 1, WHICH SIGN DO YOU WANT? [X/O]\n")
        if player_1_sign.upper() == 'X' or player_1_sign.upper() == 'O':
            break
        else:
            print("TRY AGAIN, THIS SIGN IS NOT VALID")
    print(f"player1 sign is {player_1_sign}")
    return player_1_sign


def determine_player_2_sign(player_1_sign):
    """
    function to determine player 2 sign
    :return: player 2 sign
    """
    if player_1_sign.upper() == 'X':
        player_2_sign = 'O'
    else:
        player_2_sign = 'X'
    return player_2_sign


def get_position_to_mark(list):
    """
     get position from the user, validate it, and return it to mark process
    :return: valid position to fill
    """
    while True:
        position = int(input("Enter the position you want to mark: [1-9]"))  # should be 1-9
        if list[position] == True:
            print("the position is taken")
            # if list[1] == True and list[2]== True and list[3] == True and list[4] == True and list[5] == True\
            #   and list[6] == True and list[7] == True and list[8] == True and list[9] == True:
            # print("The game is equal")
            #  exit()
            continue
        if position > 0 and position < 10:
            list[position] = True
            return position
        else:
            print("the position is not in the range")


def print_grid(board):
    """
    printing the board
    :param board: the board
    :return: none
    """
    print(f'{board[7]}|{board[8]}|{board[9]}|\n{board[4]}|{board[5]}|{board[6]}|\n'
          f'{board[1]}|{board[2]}|{board[3]}|\n')


def greet():
    """
    Greeting the winner
    :return: none
    """
    print("GONGRATULATIONS YOU WON!")


def main():
    new_position = 0
    # array holding the position usage
    position_usage = [True, False, False, False, False, False, False, False, False, False]

    # array holding the current borad status
    board_status = [' '] * 10

    # initialize players sign
    player1_sign = ""
    player2_sign = ""

    # variable for the game event loop
    var_of_stop = False
    explain()
    # determine players signs
    player1_sign = determine_player_1_sign()
    player2_sign = determine_player_2_sign(player1_sign)
    # determine which player is the first to play
    starting_player = random_first_player()
    # variable to manage turns
    counter = starting_player
    # prints empty board
    print_grid(board_status)

    while (var_of_stop != True):
        new_position = get_position_to_mark(position_usage)
        if counter % 2 != 0:
            mark_input(player1_sign, new_position, board_status)
            print_grid(board_status)
            var_of_stop = is_winning(board_status, player1_sign)
            if var_of_stop == True:
                greet()
        else:
            mark_input(player2_sign, new_position, board_status)
            print_grid(board_status)
            var_of_stop = is_winning(board_status, player2_sign)
            if var_of_stop == True:
                greet()
        if all(item for item in position_usage):
            print("Game over")
            exit()

        counter += 1

    print("game over")


if __name__ == '__main__':
    main()
