from tictactoe import Board

def main():
    counter = 1
    board = Board()
    while not board.check_game_end():
        board.display_board()
        if counter % 2 == 0:
            cell = input("Player 2, enter cell number: ")
            symbol = "X"
            
        else:
            cell = input("Player 1, enter cell number: ")
            symbol = "O"

        while not board.check_cell(cell):
                cell = input("Invalid cell, please reinput: ")

        board.update_board(cell, symbol)
        print()
        board.display_board()
        counter += 1
    
    print(board.get_outcome())

main()
