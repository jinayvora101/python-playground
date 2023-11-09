<span style="font-family: 'Cascadia Code'">



# `Main Loop Logic`
* Initialise the board
* Add a tile (if the last input wasn't undo action)
* Print the current state of the board
* Take the direction input from the user
* Waits till the user inputs a valid character
* If there is no space to push tiles in the direction specified by the input, the loop waits for another valid input



## `addTile()`
Randomly selecting a tile, and populating, randomly, with `2` or `4`



## `decodeInput()`
Accepting a single character input

Inputs:
* Numpad Keys: `2, 4, 6, 8`
* Arrow Keys: `UP, DOWN, LEFT, RIGHT`
* Game Keys: `w, a, s, d`

Special Inputs:
* Undo: `z`
* Exit/Quit: `q`



## `pushTiles()`
Accepts an `int` parameter that specifies the direction the tiles need to be pushed

Uses a sister function `mergeRow()` to compress one row at a time



## `endGameCheck()`
Return `False` and stops the loop if there is no empty tiles for `addTile()`

Or `2048` tile has been reached



## `printBoard()`
Pretty printing the `board` to the console

Cleaning the console of the previously printed `board` before pretty printing the current state of the board



## `createNewGame()`
Create a 4x4 board, populated with `None`

Calling `addTile()` twice, randomly populating two tiles



</span>
