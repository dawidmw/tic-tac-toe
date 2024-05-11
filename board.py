import random

class GameBoard:

    def __init__(self):
        self.round = 1
        self.board = {1: "1", 2: "2", 3: "3",
                      4: "4", 5: "5", 6: "6",
                      7: "7", 8: "8", 9: "9"}

    def draw_board(self):
        for n in range(len(self.board)):
            if n == 3 or n == 6:
                print()
            print(f"{self.board[n+1]} ", end="")
        print("\n" * 2)

    def choose_number(self, x_mark, o_mark):
        player_choice = int(input("Please choose a number from the board: "))
        if 0 < player_choice <= 9:
            if self.board[player_choice] != x_mark and self.board[player_choice] != o_mark:
                self.board[player_choice] = x_mark
                self.round += 1
                self.draw_board()
            else:
                print("Number already marked.")
                self.choose_number()
        else:
            print("Choose number on the board.")
            self.choose_number()

    def let_npc_play(self, o_mark, x_mark):
        empty_fields = []
        for key in self.board:
            if self.board[key] != x_mark and self.board[key] != o_mark:
                empty_fields.append(key)
        if not empty_fields:
            print("Game finished.")
            exit()
        else:
            npc_choice = random.choice(empty_fields)
            self.board[npc_choice] = o_mark
            self.round += 1
            self.draw_board()

    def check_win_conditions(self, player):
        p = player
        board = self.board

        # horizontal win
        if (board[1] == board[2] == board[3] == p) or (board[4] == board[5] == board[6] == p) or board[7] == board[8] == board[9] == p:
            return True
        # vertical win
        elif (board[1] == board[4] == board[7] == p) or (board[2] == board[5] == board[8] == p) or (board[3] == board[6] == board[9] == p):
            return True
        # diagonal win
        elif (board[1] == board[5] == board[9] == p) or (board[3] == board[5] == board[7] == p):
            return True
