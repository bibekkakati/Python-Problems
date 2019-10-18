# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and
# many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print
# statement.
row = int(input("Enter the row number : "))
column = int(input("Enter the column number : "))

def game_board():
    print((" ---")*column)
    print(("|   ")*(column+1))
    return ((" ---") * column)

for i in range(row-1):
    game_board()

print(game_board())
