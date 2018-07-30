from White import White
from Black import Black
import random
import copy

class Board():

	def __init__(self):
		self.boardMap = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
		self.white = White()
		self.black = Black()
		self.status = self.initBoard()
		# while (not self.checkPosition(self.status)):
		# 	self.status = self.initBoard()
		self.initOutPut()

	# get current status of the board
	def getStatus(self):
		return self.status

	# generate initial postions
	def initBoard(self):
		board = []
		ranPos = self.randomPositions()
		# print(ranPos)
		posCt = 0
		for i1 in range(0,8):
			row = []
			for i2 in range(0,8):
				if ranPos[0]==posCt+i2:
					row.append(11)    
				elif ranPos[1]==posCt+i2:
					row.append(12)
				elif ranPos[2]==posCt+i2:
					row.append(21)
				else:
				    row.append(0)
			posCt += 8
			board.append(row)
		return board

	# 1 -> White King, 2 -> White Rook, 3 -> Black King
	def randomPositions(self):
		randomList = [46, 63, 35]
		count = 0
		# while (count < 3):	
		# 	ran = random.randint(0,63)
		# 	if self.checkRandomList(randomList, ran):
		# 		randomList.append(ran)
		# 		count += 1
		return randomList

	# check position duplicate
	def checkRandomList(self, list, ele):
		for i in list:
			if i == ele:
				return False
		return True

	# Make sure black king has not been check
	def checkPosition(self, list):
		whiteKing = self.getPosition(list, 11)
		whiteRook = self.getPosition(list, 12)
		blackKing = self.getPosition(list, 21)
		if whiteRook[0] == blackKing[0] or whiteRook[1] == blackKing[1]:
			return False
		if (abs(whiteKing[0] - blackKing[0]) <= 1) and (abs(whiteKing[1] - blackKing[1])<=1):
			return False
		return True

	# Return position of a chessman
	def getPosition(self, list, ele):
		for i1 in range(0,8):
			for i2 in range(0,8):
				if list[i1][i2] == ele:
					return [i1, i2]

		return []


	# Write initial status in the output file
	def initOutPut(self):
		with open("output.txt", "w") as f:
		
			for i1 in range(0,8):
				for i2 in range(0,8):
					f.write(str(self.status[i1][i2]))
					f.write("\t")
				f.write("\n") 

		f.closed
		return

	# Append a move in the output file
	def writeMoves(self, originalList, movedList):
		whiteKing_before = self.getPosition(originalList, 11)
		whiteRook_before = self.getPosition(originalList, 12)
		blackKing_before = self.getPosition(originalList, 21)
		whiteKing_after = self.getPosition(movedList, 11)
		whiteRook_after = self.getPosition(movedList, 12)
		blackKing_after = self.getPosition(movedList, 21)
			
			

		with open("output.txt", "a") as f:
			if whiteKing_after!=[] and self.isMoved(whiteKing_before, whiteKing_after):
				f.write("WK\t"+self.boardMap[whiteKing_after[1]]+","+str(whiteKing_after[0]+1)+"\t\n")
			if whiteRook_after!=[] and self.isMoved(whiteRook_before, whiteRook_after):
				f.write("WH\t"+self.boardMap[whiteRook_after[1]]+","+str(whiteRook_after[0]+1)+"\t\n")
			if blackKing_after!=[] and self.isMoved(blackKing_before, blackKing_after):
				f.write("BK\t"+self.boardMap[blackKing_after[1]]+","+str(blackKing_after[0]+1)+"\t\n")
		f.close
		return

	# Check the status if the match finishes
	def checkStatus(self, originalList, movedList):
		whiteKing_after = self.getPosition(movedList, 11)
		whiteRook_after = self.getPosition(movedList, 12)
		blackKing_after = self.getPosition(movedList, 21)

		if whiteKing_after==[] or whiteRook_after==[] or blackKing_after==[]:
			self.writeMoves(originalList, movedList)
			if whiteKing_after==[]:
				return "Your Lose"
			if whiteRook_after==[]:
				return "Draw game"
			if blackKing_after==[]:
				return "You Win"
		else:
			return "Wrong move"




	# Run the match
	def play(self):
		# while (true):
		for i in range(0,12):
			# print(self.status)
			whiteMove = copy.deepcopy(self.status)
			self.white.go(whiteMove,i)
			if self.checkMove(self.status, whiteMove):
				self.writeMoves(self.status, whiteMove)
				self.status = whiteMove
			else:
				# print(whiteMove)
				return self.checkStatus(self.status, whiteMove)
				break
			
			blackMove = copy.deepcopy(self.status)
			self.black.go(blackMove)
			# print(blackMove)
			if self.checkMove(self.status, blackMove):
				self.writeMoves(self.status, blackMove)
				self.status = blackMove
			else:
				return self.checkStatus(self.status, blackMove)
				break




	# Check if a move is right or not
	def checkMove(self,originalList, movedList):
		whiteKing_before = self.getPosition(originalList, 11)
		whiteRook_before = self.getPosition(originalList, 12)
		blackKing_before = self.getPosition(originalList, 21)
		whiteKing_after = self.getPosition(movedList, 11)
		whiteRook_after = self.getPosition(movedList, 12)
		blackKing_after = self.getPosition(movedList, 21)


		# if one of these gone, end game
		if whiteKing_after==[] or whiteRook_after==[] or blackKing_after==[]:
			return False
		# if more than two chessmans move at once, end game
		if not (self.isMoved(whiteKing_before,whiteKing_after)^self.isMoved(whiteRook_before,whiteRook_after)^self.isMoved(blackKing_before,blackKing_after)):
			# print(whiteRook_before)
			# print(whiteRook_after)
			return False

		if self.isMoved(whiteKing_before,whiteKing_after) and self.isMoved(whiteRook_before,whiteRook_after) and self.isMoved(blackKing_before,blackKing_after): 
			return False


		# if all of these stay the same, end game
		# if (whiteKing_before[0]==whiteKing_after[0] and whiteKing_before[1]==whiteKing_after[1] and whiteRook_before[0]==whiteRook_after[0] and whiteRook_before[1]==whiteRook_after[1] and blackKing_before[0]==blackKing_after[0] and blackKing_before[1]==blackKing_after[1]):
		# 	return False

		#if the king goes wrong move, end game
		if whiteRook_before[0]!=whiteRook_after[0] and whiteRook_before[1]!=whiteRook_after[1]:
			return False

		#if the Rook goes wrong move, end game
		if abs(whiteKing_before[0]-whiteKing_after[0])>1 or abs(whiteKing_before[1]-whiteKing_after[1])>1:
			return False

		#if the king goes wrong move, end game
		if abs(blackKing_before[0]-blackKing_after[0])>1 or abs(blackKing_before[1]-blackKing_after[1])>1:
			return False
		return True

	def isMoved(self, before, after):
		if before[0]==after[0] and before[1]==after[1]:
			return False
		return True