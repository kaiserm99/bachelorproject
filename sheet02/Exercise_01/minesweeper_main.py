from minesweeper_board import *
from minesweeper_csp import *
import argparse

def main(args):
    if args.board is None:
        board = Board(10,10)
        board.insert_bomb(3,1)
        board.insert_bomb(5,1)
        board.insert_bomb(5,2)
        board.insert_bomb(5,4)
        board.insert_bomb(1,5)
        board.insert_bomb(2,5)
        board.insert_bomb(5,5)
        board.insert_bomb(8,8)
        board.insert_bomb(8,9)
        board.insert_bomb(3,8)
        board.insert_bomb(8,3)
    else: 
        board = Board(args.board[0],args.board[0])
        board.random_board(args.board[1])
    print("Selcted cell: " + str((0,0)))
    board.uncover_cell(0,0)
    if not args.fast:
        board.dump()
    while not board.is_solved():
        if not args.fast:
            input("Press Enter to continue...")
            print("-----------------------------")
        csp = Csp(board)
        next_cell = csp.next_cell()
        print("Selcted cell: " + str(next_cell))
        success = board.uncover_cell(next_cell[0], next_cell[1])
        if not success:
            print("Select cell is a bombe! FAIL!")
            break
        if not args.fast:
            board.dump()
            print()
        
    if board.is_solved():
        print("-----------------------------")
        print("-----------------------------")
        print("SOLVED!!!")
        board.dump()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", help="fast mode", action="store_true")
    parser.add_argument("--board", help="random board with d n: d=dimensions, m=#mines", nargs='+', type=int)
    args = parser.parse_args()
    main(args)
