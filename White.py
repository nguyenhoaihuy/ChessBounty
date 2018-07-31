class White():

	def _init_(self):
		self.count = 0

	def go(self, movedList):
		self.decide(movedList)

	# This function is do a move from a position 'source' to other posision 'destination' in board 'list'
	# It will return a new list
	# Only one move 
	def move(self, list, source, destination):
		list[destination[0]][destination[1]]=list[source[0]][source[1]]
		list[source[0]][source[1]] = 0
		return list


	def decide(self, boardStatus):
		'''
		Your work should be implemented here
		'''


