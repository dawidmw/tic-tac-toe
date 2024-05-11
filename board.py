import random

PLAYER_MARK = "X"
NPC_MARK = "◯"


class GameBoard:

    def __init__(self):
        self.player_mark = PLAYER_MARK
        self.npc_mark = NPC_MARK
        self.round = 1
        self.board = {1: "1", 2: "2", 3: "3",
                      4: "4", 5: "5", 6: "6",
                      7: "7", 8: "8", 9: "9"}

    def draw_board(self):
        for n in range(len(self.board)):
            if n == 3 or n == 6:
                print()
            print(f"{self.board[n + 1]} ", end="")
        print("\n" * 2)

    def choose_number(self):
        player_choice = int(input("Please provide a number: "))
        if player_choice in self.check_for_empty_fields():
            self.board[player_choice] = self.player_mark
            self.round += 1
            self.draw_board()
            if self.check_win_conditions(self.player_mark):
                print("Player has won the match.")
                exit()
        else:
            print("Please select a valid number.")
            self.choose_number()

    def let_npc_play(self):
        npc_choice = random.choice(self.check_for_empty_fields())
        self.board[npc_choice] = self.npc_mark
        self.round += 1
        self.draw_board()
        if self.check_win_conditions(self.npc_mark):
            print("NPC has won the match.")
            exit()

    def check_win_conditions(self, player):
        p = player
        board = self.board

        # horizontal win
        if (board[1] == board[2] == board[3] == p) or (board[4] == board[5] == board[6] == p) or board[7] == board[8] == \
                board[9] == p:
            return True
        # vertical win
        elif (board[1] == board[4] == board[7] == p) or (board[2] == board[5] == board[8] == p) or (
                board[3] == board[6] == board[9] == p):
            return True
        # diagonal win
        elif (board[1] == board[5] == board[9] == p) or (board[3] == board[5] == board[7] == p):
            return True

    def check_for_empty_fields(self):
        empty_fields = []
        for key in self.board:
            if self.board[key] != self.player_mark and self.board[key] != self.npc_mark:
                empty_fields.append(key)
        if not empty_fields:
            print("Game finished in a tie.")
            exit()
        else:
            return empty_fields

    def choose_first_player(self):
        self.round = random.randint(1, 2)
