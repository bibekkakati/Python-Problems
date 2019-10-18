# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more
#  than half an hour of coding, so we’re doing it in pieces. Today, we will simply focus on checking whether someone
# has WON a game of Tic Tac Toe, not worrying about how the moves were made. If a game of Tic Tac Toe is represented
# as a list of lists, like so:
# game = [[1, 2, 0],
#         [2, 1, 0],
#        [2, 1, 1]]
# where a 0 means an empty square,
# a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
# has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column,
# or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be
#  one winner.
import random

list_1 = (random.sample(range(3),3))
list_2 = (random.sample(range(3),3))
list_3 = (random.sample(range(3),3))

game = [list_1, list_2, list_3]


def play_game():
    for i in range(1, 3):
        if list_1[i] == list_2[i] == list_3[i]:
            return str(i) + ' is the winner'
        else:
            return 'No one wins.'


print(game)
print(play_game())
