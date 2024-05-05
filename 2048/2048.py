from os import system
from itertools import product, chain
from random import choice, shuffle
from numpy import full, array, array_equal
from readchar import readkey, key



def createNewGame():

    global board
    board = full((4, 4), None)
    addTile()
    addTile()



def addTile():

    itr = list(product(range(4), range(4)))
    shuffle(itr)

    for i, j in itr:
        if board[i, j] is None:
            board[i, j] = choice([2, 2, 4, 4, 4])
            break



def decodeInput():

    print("enter input:")
    x = readkey()

    if x.isnumeric() and int(x) in [2, 4, 6, 8]:
        return int(x)

    elif x in [key.DOWN, key.LEFT, key.RIGHT, key.UP]:
        return ([key.DOWN, key.LEFT, key.RIGHT, key.UP].index(x) + 1) * 2

    elif x in ["s", "a", "d", "w"]:
        return (["s", "a", "d", "w"].index(x) + 1) * 2

    elif x == "q":
        return "exit"

    elif x == "z":
        return "undo"

    else:
        print("retry inputting...")
        return decodeInput()



def pushTiles(dir_):

    if dir_ == 2:
        for i in range(4): board[:, i] = mergeRow(board[:, i][::-1])[::-1]

    elif dir_ == 8:
        for i in range(4): board[:, i] = mergeRow(board[:, i])

    elif dir_ == 6:
        for i in range(4): board[i, :] = mergeRow(board[i, :][::-1])[::-1]

    elif dir_ == 4:
        for i in range(4): board[i, :] = mergeRow(board[i, :])



def mergeRow(tmp):

    tmp = tmp.tolist()
    ptr1, ptr2 = 0, 1

    while (ptr1 < 3) and (ptr2 <= 3):

        if tmp[ptr1] is None:
            ptr1 += 1
            ptr2 = ptr1+1

        elif tmp[ptr2] is None:
            ptr2 += 1

        elif tmp[ptr1] == tmp[ptr2]:
            tmp[ptr1] *= 2
            tmp[ptr2] = None
            ptr1 += 1
            ptr2 = ptr1+1

        elif tmp[ptr1] != tmp[ptr2]:
            ptr1 = ptr2
            ptr2 = ptr1+1

    tmp = list(filter(lambda x: x is not None, tmp))
    tmp = tmp + [None]*(4-len(tmp))

    return array(tmp)



def endGameCheck():

    global board

    flat = list(chain(*board))

    if 2048 in flat:
        print("You Won!\n========")

    elif None in flat: return True

    else: return False



def printBoard():

    global board

    system("clear")

    print(" " + "".join(["-"]*29))

    for i in board:

        print(" | ", end="")

        for j in i:
            print(str(j).rjust(4, " ") if j is not None else "    ", end=" | ")

        print("\n "+"".join(["-"]*29))



inp = "undo"
board, prevBoard = array([]), array([])

createNewGame()

while endGameCheck():

    if inp != "undo": addTile()

    printBoard()

    inp = decodeInput()

    while True:

        if inp in [2, 4, 6, 8]:

            prevBoard = board.copy()
            pushTiles(inp)

            if not array_equal(prevBoard, board): break

            print("can't push in that direction")
            inp = decodeInput()

        elif inp == "undo":

            board = prevBoard.copy()
            break

        elif inp == "exit":

            from sys import exit
            exit()

        else:
            inp = decodeInput()

printBoard()



