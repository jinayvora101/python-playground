<span style="font-family: 'Cascadia Code'">



# `Main Loop Logic`
* Initialise the board
* Print the board and wait for the first player's valid input
* Check the game status
* Repeat these steps for the second player
* Continue the cycle till the game status changes



## `decodeInput()`
Accepting two continous numerical characters, respresenting the co-ordinates on the board

Inputs:
* `11, ..., 13, ..., 33`: Nine possible inputs. First charcter represents row number, second number represents column number
* Exit: `q`



## `addTile()`
Adding the current player symbol on the board corresponding co-ordinates inputted



## `printBoard()`
Pretty printing the `board` to the console

Cleaning the console of the previously printed `board` before pretty printing the current state of the board



## `checkStatus()`
Checks if any rows, columns, or diagonals are occupied by the symbols of the same player.



</span>
