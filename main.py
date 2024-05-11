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

    player_mark = "X"
    npc_mark = "◯"

    while game_on:
        if game_board.round % 2 != 0:
            game_board.choose_number(player_mark, npc_mark)
            if game_board.check_win_conditions(player_mark):
                print("Player has won the match.")
                exit()
        elif game_board.round % 2 == 0:
            game_board.let_npc_play(npc_mark, player_mark)
            if game_board.check_win_conditions(npc_mark):
                print("NPC has won the match.")
                exit()


if __name__ == '__main__':
    get_logo_and_rules()
