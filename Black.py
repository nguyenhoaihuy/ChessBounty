import math 
class Black():

	def _init_(self):
		self.count = 0
		
	def go(self, boardStatus):
		return self.decide(boardStatus)

	def decide(self, boardStatus):
		corner = self.checkCorner(boardStatus)
		possibilities = self.getPossibilities(boardStatus,21)
		whiteKingPossibilities = self.getPossibilities(boardStatus,11)
		blackKing = self.getPosition(boardStatus, 21)

		self.kingvsking(possibilities, whiteKingPossibilities)
		self.kingvsrook(possibilities, boardStatus)
		self.getCloseToRook(possibilities, boardStatus)
		self.beatKing(possibilities, boardStatus)
		# self.beatRook(possibilities, boardStatus)
		
		nextMove = self.nextMove(possibilities)
		# print(possibilities)
		# print(nextMove)
		self.move(boardStatus, blackKing, nextMove)
		# print(boardStatus)
		# print(possibilities)
		return boardStatus

	def nextMove(self, blackKing):
		holder = blackKing[0]
		rate = holder[2]
		for item in blackKing:
			if (rate < item[2]):
				rate = item[2]
				holder = item
		return [holder[0],holder[1]]

	def beatKing(self, blackKing, boardStatus):
		whiteKing = self.getPosition(boardStatus, 11)
		for item1 in blackKing:
			if whiteKing[0]==item1[0] and whiteKing[1]==item1[1]:
				item1[2] += 100

	def beatRook(self, blackKing, boardStatus):
		whiteRook = self.getPosition(boardStatus, 12)
		for item1 in blackKing:
			if whiteRook[0]==item1[0] and whiteRook[1]==item1[1]:
				print("hello")
				item1[2] += 20

	def kingvsking(self, blackKing, whiteKing):
		for item1 in blackKing:
			for item2 in whiteKing:
				if item1[0]==item2[0] and item1[1]==item2[1]:
					item1[2] -= 50
		return

	def kingvsrook(self, blackKing, boardStatus):
		whiteRook = self.getPosition(boardStatus, 12)
		for item1 in blackKing:
			if item1[0] == whiteRook[0] and item1[1] == whiteRook[1]:
				item1[2]+= 80
				
			if item1[0] == whiteRook[0]:
				item1[2]-= 30

			if item1[1] == whiteRook[1]:
				item1[2]-= 30
		return

	def getCloseToRook(self,blackKing,boardStatus):
		whiteRook = self.getPosition(boardStatus, 12)
		for item1 in blackKing:
			item1[2] -= self.distance([item1[0],item1[1]],whiteRook)/2
		return

	def checkCorner(self, boardStatus):
		list_corners = [[0,0],[0,7],[7,0],[7,7]]
		whiteKing = self.getPosition(boardStatus, 11)
		whiteRook = self.getPosition(boardStatus, 12)
		blackKing = self.getPosition(boardStatus, 21)

		if whiteRook[0]==blackKing[0] and whiteRook[1]<blackKing[1]:
			if self.distance(blackKing, list_corners[1])<self.distance(blackKing, list_corners[3]):
				return list_corners[3]
			else:
				return list_corners[1]
		if whiteRook[0]==blackKing[0] and whiteRook[1]>blackKing[1]:	
			if self.distance(blackKing, list_corners[0])<self.distance(blackKing, list_corners[2]):
				return list_corners[2]
			else:
				return list_corners[0]

		if whiteRook[1]==blackKing[1] and whiteRook[0]<blackKing[0]:
			if self.distance(blackKing, list_corners[2])<self.distance(blackKing, list_corners[3]):
				return list_corners[3]
			else:
				return list_corners[2]
		if whiteRook[1]==blackKing[1] and whiteRook[0]>blackKing[0]:	
			if self.distance(blackKing, list_corners[0])<self.distance(blackKing, list_corners[1]):
				return list_corners[1]
			else:
				return list_corners[0]

		if whiteRook[0]>blackKing[0] and whiteRook[1]>blackKing[1]:
			return list_corners[0]

		if whiteRook[0]>blackKing[0] and whiteRook[1]<blackKing[1]:
			return list_corners[1]

		if whiteRook[0]<blackKing[0] and whiteRook[1]>blackKing[1]:
			return list_corners[2]

		if whiteRook[0]<blackKing[0] and whiteRook[1]<blackKing[1]:
			return list_corners[3]

		return []


	def getPossibilities(self, boardStatus,ele):
		result = []
		blackKing = self.getPosition(boardStatus, ele)

		if blackKing[0]-1>=0 and blackKing[1]-1>=0:
			result.append([blackKing[0]-1,blackKing[1]-1,10])

		if blackKing[0]-1>=0:
			result.append([blackKing[0]-1,blackKing[1],10])

		if blackKing[0]-1>=0 and blackKing[1]+1<=7:
			result.append([blackKing[0]-1,blackKing[1]+1,10])

		if blackKing[1]+1<=7:
			result.append([blackKing[0],blackKing[1]+1,10])

		if blackKing[0]+1<=7 and blackKing[1]+1<=7:
			result.append([blackKing[0]+1,blackKing[1]+1,10])

		if blackKing[0]+1<=7:
			result.append([blackKing[0]+1,blackKing[1],10])

		if blackKing[0]+1<=7 and blackKing[1]-1>=0:
			result.append([blackKing[0]+1,blackKing[1]-1,10])

		if blackKing[1]-1>=0:
			result.append([blackKing[0],blackKing[1]-1,10])

		return result

	def distance(self, cell1, cell2):
		x = abs(cell1[1]-cell2[1])
		y = abs(cell1[0]-cell2[0])
		result = math.sqrt(x*x+y*y)
		return result

	def getPosition(self, list, ele):
		for i1 in range(0,8):
			for i2 in range(0,8):
				if list[i1][i2] == ele:
					return [i1, i2]

		return []

	def move(self, list, source, destination):
		list[destination[0]][destination[1]]=list[source[0]][source[1]]
		list[source[0]][source[1]] = 0
		return list