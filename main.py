from board import GameBoard
from logos import logo
import os


def get_logo_and_rules():
    print(logo)
    print(
        f"Welcome to text based Tic-Tac-Toe.\nHere are some rules to get you started:\n1. You are X, NPC plays ◯.\n2. "
        f"You play by inputting the number provided on the board.\n3. If no one scores three in a row or diagonally the "
        f"game ends in a tie.\n")
    play_game = input("Type 's' to start. Type 'q' to exit: ")
    if play_game == "s":
        print()
        main()
    elif play_game == "q":
        exit()

def main():
    game_on = True
    game_board = GameBoard()
    game_board.draw_board()
    game_board.choose_first_player()

    while game_on:
        if game_board.round % 2 != 0:
            game_board.choose_number()
        elif game_board.round % 2 == 0:
            game_board.let_npc_play()


if __name__ == '__main__':
    get_logo_and_rules()
