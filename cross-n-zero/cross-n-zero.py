from numpy import array, full, array_equal, diag



board = full((3, 3), "_")



def decodeInput(player):

    inp = input(f"Player {player}: input >> ")

    if inp == "q": return -1

    try:

        inp = tuple(int(i)-1 for i in list(inp) if int(i)>0)
        if len(inp) != 2: raise Exception()
        if board[inp] != "_": raise Exception()

    except:

        print("retry inputting...")
        inp = decodeInput(player)

    return inp



def printBoard():

    string = [" "+" | ".join(i)+" " for i in board]
    sep = "\n---+---+---\n"
    string = sep.join(string).replace("_", " ")
    print(string)



def addTile(player, inp):

    board[inp] = player



def checkStatus():

    xs = array(["x", "x", "x"])
    os = array(["o", "o", "o"])
    
    for i in range(3):

        if array_equal(board[i, :], xs) or array_equal(board[:, i], xs):
            print("Player x won")
            return "break"

        elif array_equal(board[i, :], os) or array_equal(board[:, i], os):
            print("Player o won")
            return "break"

    if array_equal(diag(board), xs) or array_equal(diag(board[::-1]), xs):
        print("Player x won")
        return "break"

    elif array_equal(diag(board), os) or array_equal(diag(board[::-1]), os):
        print("Player o won")
        return "break"

    if "_" not in board.flatten():
        print("Game Tied")
        return "break"

    return "continue"



""" Game Loop """

while True:

    """ Player x turn """

    printBoard()

    inp = decodeInput("x")

    if inp == -1:
        print("Exit")
        break

    addTile("x", inp)

    if checkStatus() == "break":
        printBoard()
        break


    """ Player o turn """

    printBoard()

    inp = decodeInput("o")

    if inp == -1:
        print("Exit")
        break

    addTile("o", inp)

    status = checkStatus()

    if checkStatus() == "break":
        printBoard()
        break


