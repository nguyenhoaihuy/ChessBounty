class White():

	def _init_(self):
		self.count = 0

	def go(self, movedList,i):
		self.decide(movedList,i)

	def decide(self, boardStatus,i):
		# print(boardStatus)
		if i==0:
			boardStatus1 = self.move(boardStatus,[7,7],[7,4])
		if i==1:
			boardStatus1 = self.move(boardStatus,[5,6],[6,5])
		if i==2:
			boardStatus1 = self.move(boardStatus,[7,4],[5,4])
		if i==3:
			boardStatus1 = self.move(boardStatus,[5,4],[6,4])
		if i==4:
			boardStatus1 = self.move(boardStatus,[6,5],[7,4])
		if i==5:
			boardStatus1 = self.move(boardStatus,[6,4],[6,3])
		if i==6:
			boardStatus1 = self.move(boardStatus,[7,4],[6,4])
		if i==7:
			boardStatus1 = self.move(boardStatus,[6,4],[7,3])
		if i==8:
			boardStatus1 = self.move(boardStatus,[6,3],[6,2])
		if i==9:
			boardStatus1 = self.move(boardStatus,[7,3],[6,3])
		if i==10:
			boardStatus1 = self.move(boardStatus,[6,3],[7,2])
		if i==11:
			boardStatus1 = self.move(boardStatus,[6,2],[6,0])
		# print(boardStatus)
		return boardStatus1

	
	def move(self, list, source, destination):
		list[destination[0]][destination[1]]=list[source[0]][source[1]]
		list[source[0]][source[1]] = 0
		return list
