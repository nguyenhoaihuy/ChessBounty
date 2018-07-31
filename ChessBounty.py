from Board import Board
from BoardUI import BoardUI
import sys

output = "output.txt"
if (len(sys.argv)==2):
	if (sys.argv[1]=="-t"):
		output = "test.txt"
board = Board()

print(board.play())
# print(board.getStatus())

boardui = BoardUI(output)
boardui.show()

