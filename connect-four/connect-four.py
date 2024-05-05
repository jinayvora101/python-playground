from sys import exit
from sys import stdout
import numpy as np
from tabulate import tabulate



class Player:

    def __init__(self, userid):
        self.userid = userid


    def registerBoard(self, board):
        self.board = board


    def inputHandler(self):
        """Keeps asking for correct input as long as `Board.inputHandler()` is not satisfied
        """

        acknowledge = False
        while not acknowledge:
            try:
                column = input(f"Player {self.userid}: Enter the column number between 1 and 7: ")
                self.board.inputHandler(self.userid, column)
                acknowledge = True
            except Exception as e: print(e)



class Board:

    def __init__(self):
        self.board = np.zeros(shape=(6, 7), dtype=np.int8)


    def registerPlayers(self,
                        player1: Player,
                        player2: Player):

        self.symbols = { player1.userid: 1, player2.userid: -1 }
        self.symbols_backlink = { 1: player1.userid, -1: player2.userid }


    def columnEntry(self,
                    symbol: int,
                    column: int) -> tuple[int, int]:
        """Play the `Player`'s turn

        Args:
            symbol (int): +/-1 representation of the two `Player`s
            column (int): acceptable column values between 0 and 6

        Raises:
            Exception: throws exception in case the mentioned column is full

        Returns:
            (int, int): (row, column)
        """

        if self.board[0, column] != 0:
            raise Exception("Column Error: No space in the specified column")

        row = np.argwhere(self.board[:, column] == 0).max()
        self.board[row, column] = symbol

        return row, column
    

    def checkFourConsecutive(self,
                             array: np.ndarray,
                             symbol: int) -> bool:
        """Checks if the input `array` has atleast 4 consecutive elements of the `symbol`

        Args:
            array (np.ndarray): input array
            symbol (int): +/-1 representation of the two `Player`s

        Returns:
            bool: `True`, if found, else `False`
        """

        idx = np.argwhere(array == symbol).flatten()
        dif = np.diff(idx)

        if dif.__eq__(1).sum() >= 3:
            return True

        return False


    def checkStatus(self,
                    symbol: int,
                    row: int,
                    column: int) -> int:
        """Checks if the win condition or tie condition have been met

        Args:
            symbol (int): +/-1 representation of the two `Player`s
            row (int): acceptable row values between 0 and 5
            column (int): acceptable column values between 0 and 6

        Returns:
            int: +1 -> current `Player` has won the game. -1 -> game is tied. 0 -> continue the game
        """

        if self.checkFourConsecutive(self.board[:, column], symbol) \
        or self.checkFourConsecutive(self.board[row, :], symbol) \
        or self.checkFourConsecutive(np.diag(self.board, k=column-row), symbol) \
        or self.checkFourConsecutive(np.diag(np.fliplr(self.board), k=row-column-2), symbol):
            return 1 # win condition met
        
        if np.equal(self.board, 0).sum() == 0:
            return -1 # tie condition met

        else: return 0


    def inputHandler(self, symbol, column):

        """ Check if the player symbol is correct """
        if symbol in self.symbols.keys():
            symbol = self.symbols[symbol]
        else:
            raise Exception("User Error: Unregistered user encountered")
        
        """ Check if player wants to quit the game """
        if column == "q" or column == "Q":
            print("Quitting the game...")
            exit()

        """ Check if the input is of type int and between 1 and 7 """
        try:
            column = int(column)
            if column < 1 or column > 7:
                raise Exception("Column Error: No such column exists")
        except:
            raise Exception("Column Error: Column number must be an integer")
        
        """ Enters the symbol at the specified column. Throws error if there is insufficient space in the column to add symbol """
        row, column = self.columnEntry(symbol, column-1)

        """ Take appropriate steps if the game has ended or tied """
        status = self.checkStatus(symbol, row, column)
        if status == 1:
            erase_last_lines()
            print(self)
            print(f"Player {self.symbols_backlink[symbol]} won")
            exit()
        elif status == -1:
            erase_last_lines()
            print(self)
            print("Tie occured")
            exit()


    def __str__(self):
        tmp = self.board.astype(str)
        tmp[tmp == "1"] = "X"
        tmp[tmp == "-1"] = "O"
        tmp[tmp == "0"] = " "
        tmp = tabulate(tmp, headers=["1", "2", "3", "4", "5", "6", "7"], tablefmt="fancy_grid")
        tmp = tmp[:43] + tmp[131:-44] + tmp[87:131] + tmp[43:87] + tmp[-44:]
        return tmp



"""
    Object Initialisation
"""
board = Board()
player1 = Player(input("Enter Player 1 userid: "))
player2 = Player(input("Enter Player 2 userid: "))

"""
    Object Registering
"""
board.registerPlayers(player1=player1, player2=player2)
player1.registerBoard(board=board)
player2.registerBoard(board=board)

def erase_last_lines(n=16):
    for _ in range(n):
        stdout.write('\033[F')
        stdout.write('\033[K')

"""
    Main Game Loop
"""
while True:

    print(board)
    player1.inputHandler()

    erase_last_lines()
    print(board)
    player2.inputHandler()
    
    erase_last_lines()