class Board:
    def __init__(self):
        self.board = [[' '] * 3 for i in range(3)]
        self.winner = ""

    def display_board(self):
        board = self.getboard()
        row = "ABC"
        column = ["1", "2", "3"]
        print(f"    {" ".join(column)}")
        for i in range(3):
            print(f" {row[i]}  { "|".join(board[i])}")
        print()
        print()

    def check_cell(self, cell):
        if len(cell) != 2:
            return False
        else:
            row, column = list(cell)
            if row.upper() not in "ABC":
                return False
            elif not column.isdigit():
                return False
            elif column not in "123":
                return False
        
        board = self.getboard()
        row, column = self.convert_cell(cell)
        if board[row][int(column)] != " ":
            return False
        else:
            return True
            
    def convert_cell(self, cell):
        row, column = list(cell)
        if row.upper() == "A":
            row = 0
        elif row.upper() == "B":
            row = 1
        else:
            row = 2
        column = int(column) - 1
        return row, column
    
    def getboard(self):
        return self.board
    
    def update_board(self, cell, symbol):
        row, column = self.convert_cell(cell)
        self.board[row][column] = symbol
    
    def check_winner(self):
        board = self.getboard()
        for i in range(3):
            #check if there is a win in rows
            if board[i][0] == board[i][1] == board[i][2] != " ":
                self.set_winner(board[i][0])
                return True
            #check if there is a win in columns
            elif board[0][i] == board[1][i] == board[2][i] != " ":
                self.set_winner(board[i][0])
                return True
        #check if there is a win in diagonals
        if board[0][0] == board[1][1] == board[2][2] != " ":
            self.set_winner(board[0][0])
            return True
        elif board[0][2] == board[1][1] == board[2][0] != " ":
            self.set_winner(board[0][2])
            return True
        return False
    
    def set_winner(self, symbol):
        if symbol == "O":
            self.winner = "Player 1"
        else:
            self.winner = "Player 2"
        
    def get_outcome(self):
        if self.winner == "":
            return "It's a Tie!"
        else:
            return f"{self.winner} is the winner! Good Job! :)"
    
    def check_game_end(self):
        if self.check_winner():
            return True
        board = self.getboard()
        for row in board:
            if " " in row:
                return False
        return True
