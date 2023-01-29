import random


class Board:
    def __init__(self):
        self.board_num = ["1", " ", " ", "2", " ", " ", "3", "\n", "\n", "4", " ", " ",
                          "5", " ", " ", "6", "\n", "\n", "7", " ", " ", "8", " ", " ", "9", "\n", "\n"]
        self.board = ["#", " ", " ", "#", " ", " ", "#", "\n", "\n", "#", " ", " ",
                      "#", " ", " ", "#", "\n", "\n", "#", " ", " ", "#", " ", " ", "#", "\n", "\n"]
        self.default_board_drawn = False
        self.draw()

    def draw(self):
        if self.default_board_drawn == False:
            for i in self.board_num:
                print(i, end="")
            print("\n")
            self.default_board_drawn = True
        else:
            for i in self.board:
                print(i, end="")
            print("\n")

    def update(self, index, symbol):
        is_full = self.check_if_full()
        if is_full: 
            return None 
        if self.board[self.board_num.index(index)] == "#":
            self.board[self.board_num.index(index)] = symbol
            self.draw()
            return True
        else:
            print("Space already taken")
            return False

    def check_if_win(self):
        if self.board[self.board_num.index("1")] == "X" and self.board[self.board_num.index("2")] == "X" and self.board[self.board_num.index("3")] == "X":
            self.board[self.board_num.index("1")] = "-"
            self.board[self.board_num.index("2")] = "-" 
            self.board[self.board_num.index("3")] = "-" 
            self.draw()
            return 0
        if self.board[self.board_num.index("1")] == "X" and self.board[self.board_num.index("4")] == "X" and self.board[self.board_num.index("7")] == "X":
            self.board[self.board_num.index("1")] = "|"
            self.board[self.board_num.index("4")] = "|" 
            self.board[self.board_num.index("7")] = "|"
            self.draw()
            return 0
        if self.board[self.board_num.index("1")] == "X" and self.board[self.board_num.index("5")] == "X" and self.board[self.board_num.index("9")] == "X":
            self.board[self.board_num.index("1")] = "\\"
            self.board[self.board_num.index("5")] = "\\" 
            self.board[self.board_num.index("9")] = "\\"
            self.draw()
            return 0
        if self.board[self.board_num.index("2")] == "X" and self.board[self.board_num.index("5")] == "X" and self.board[self.board_num.index("8")] == "X":
            self.board[self.board_num.index("2")] = "|"
            self.board[self.board_num.index("5")] = "|" 
            self.board[self.board_num.index("8")] = "|"
            self.draw()
            return 0
        if self.board[self.board_num.index("3")] == "X" and self.board[self.board_num.index("6")] == "X" and self.board[self.board_num.index("9")] == "X":
            self.board[self.board_num.index("3")] = "|"
            self.board[self.board_num.index("6")] = "|" 
            self.board[self.board_num.index("9")] = "|"
            self.draw()
            return 0
        if self.board[self.board_num.index("4")] == "X" and self.board[self.board_num.index("5")] == "X" and self.board[self.board_num.index("6")] == "X":
            self.board[self.board_num.index("4")] = "-"
            self.board[self.board_num.index("5")] = "-" 
            self.board[self.board_num.index("6")] = "-"
            self.draw()
            return 0
        if self.board[self.board_num.index("7")] == "X" and self.board[self.board_num.index("8")] == "X" and self.board[self.board_num.index("9")] == "X":
            self.board[self.board_num.index("7")] = "-"
            self.board[self.board_num.index("8")] = "-" 
            self.board[self.board_num.index("9")] = "-"
            self.draw()
            return 0
        if self.board[self.board_num.index("3")] == "X" and self.board[self.board_num.index("5")] == "X" and self.board[self.board_num.index("7")] == "X":
            self.board[self.board_num.index("3")] = "/"
            self.board[self.board_num.index("5")] = "/" 
            self.board[self.board_num.index("7")] = "/"
            self.draw()
            return 0

        if self.board[self.board_num.index("1")] == "O" and self.board[self.board_num.index("2")] == "O" and self.board[self.board_num.index("3")] == "O":
            self.board[self.board_num.index("1")] = "-"
            self.board[self.board_num.index("2")] = "-"
            self.board[self.board_num.index("3")] = "-"
            self.draw() 
            return 1
        if self.board[self.board_num.index("1")] == "O" and self.board[self.board_num.index("4")] == "O" and self.board[self.board_num.index("7")] == "O":
            self.board[self.board_num.index("1")] = "|"
            self.board[self.board_num.index("4")] = "|" 
            self.board[self.board_num.index("7")] = "|"
            self.draw()
            return 1
        if self.board[self.board_num.index("1")] == "O" and self.board[self.board_num.index("5")] == "O" and self.board[self.board_num.index("9")] == "O":
            self.board[self.board_num.index("1")] = "\\"
            self.board[self.board_num.index("5")] = "\\" 
            self.board[self.board_num.index("9")] = "\\"
            self.draw()
            return 1
        if self.board[self.board_num.index("2")] == "O" and self.board[self.board_num.index("5")] == "O" and self.board[self.board_num.index("8")] == "O":
            self.board[self.board_num.index("2")] = "|"
            self.board[self.board_num.index("5")] = "|" 
            self.board[self.board_num.index("8")] = "|"
            self.draw()
            return 1
        if self.board[self.board_num.index("3")] == "O" and self.board[self.board_num.index("6")] == "O" and self.board[self.board_num.index("9")] == "O":
            self.board[self.board_num.index("3")] = "|"
            self.board[self.board_num.index("6")] = "|" 
            self.board[self.board_num.index("9")] = "|"
            self.draw()
            return 1
        if self.board[self.board_num.index("4")] == "O" and self.board[self.board_num.index("5")] == "O" and self.board[self.board_num.index("6")] == "O":
            self.board[self.board_num.index("4")] = "-"
            self.board[self.board_num.index("5")] = "-" 
            self.board[self.board_num.index("6")] = "-"
            self.draw()
            return 1
        if self.board[self.board_num.index("7")] == "O" and self.board[self.board_num.index("8")] == "O" and self.board[self.board_num.index("9")] == "O":
            self.board[self.board_num.index("7")] = "-"
            self.board[self.board_num.index("8")] = "-" 
            self.board[self.board_num.index("9")] = "-"
            self.draw()
            return 1
        if self.board[self.board_num.index("3")] == "O" and self.board[self.board_num.index("5")] == "O" and self.board[self.board_num.index("7")] == "O":
            self.board[self.board_num.index("3")] = "/"
            self.board[self.board_num.index("5")] = "/" 
            self.board[self.board_num.index("7")] = "/"
            self.draw()
            return 1

    def check_if_full(self):
        if self.board[self.board_num.index("1")] != "#" and self.board[self.board_num.index("2")] != "#" and self.board[self.board_num.index("3")] != "#" and self.board[self.board_num.index("4")] != "#" and self.board[self.board_num.index("5")] != "#" and self.board[self.board_num.index("6")] != "#" and self.board[self.board_num.index("7")] != "#" and self.board[self.board_num.index("8")] != "#" and self.board[self.board_num.index("9")] != "#":
            return True


class Player:
    def __init__(self, name, symbol, board):
        self.name = name
        self.symbol = symbol
        self.board = board        

    def play(self):
        print(f"{self.name} plays")
        position = input("Enter position to play in: ")
        update = self.board.update(position, self.symbol)
        if update == False:
            self.play()
        elif update == None:
            return False


class Game:
    def __init__(self, b):
        self.b = b
        self.move_map = {"heads": 0, "tails": 1}
        self.begin_turn = random.randint(0, 1)
        self.p1 = Player("Player1", "X", self.b)
        self.p2 = Player("Player2", "O", self.b)
        self.p1_score = 0
        self.p2_score = 0
        print("Use these number format to chose where you want to PLAY in")
        print("Player1 is X", end="")
        print("\t Player2 is O")  


    def begin_match(self):
        input1 = input("Heads or tails: (for player1) ").lower()
        input1 = self.move_map[input1]
        if input1 == self.begin_turn:
            self.p1.play()
            self.turn = 1
            print(f"Player1 score: {self.p1_score}", end="")
            print(f"\t Player2 score: {self.p2_score}\n")
        else:
            self.p2.play()
            self.turn = 0
            print(f"Player1 score: {self.p1_score}", end="")
            print(f"\t Player2 score: {self.p2_score}\n")
        while True:
            self.play_match()
        

    def play_match(self):
        if self.turn == 0:
            is_full = self.p1.play()
            if is_full == False:
                print("Spaces full!!")
                self.restart()
            self.turn = 1
        elif self.turn == 1:
            is_full = self.p2.play()
            if is_full == False:
                print("Spaces full!!")
                self.restart()
            self.turn = 0
        print(f"Player1 score: {self.p1_score}", end="")
        print(f"\t Player2 score: {self.p2_score}\n")
        self.check_if_winner()

    def check_if_winner(self):
        winner = self.b.check_if_win()
        if winner == 0:
            print(f"{self.p1.name} has won")
            self.p1_score += 1
            print(f"Player1 score: {self.p1_score}", end="")
            print(f"\t Player2 score: {self.p2_score}\n")
            self.restart()
        elif winner == 1:
            print(f"{self.p2.name} has won")
            self.p2_score += 1
            print(f"Player1 score: {self.p1_score}")
            print(f"Player2 score: {self.p2_score}")
            self.restart()

    def restart(self):
        self.b.board_num = ["1", " ", " ", "2", " ", " ", "3", "\n", "\n", "4", " ", " ",
                          "5", " ", " ", "6", "\n", "\n", "7", " ", " ", "8", " ", " ", "9", "\n", "\n"]
        self.b.board = ["#", " ", " ", "#", " ", " ", "#", "\n", "\n", "#", " ", " ",
                      "#", " ", " ", "#", "\n", "\n", "#", " ", " ", "#", " ", " ", "#", "\n", "\n"]
        self.move_map = {"heads": 0, "tails": 1}
        self.begin_turn = random.randint(0, 1)
        self.begin_match()

def main():        
    b = Board()
    g = Game(b)
    g.begin_match()


main()
