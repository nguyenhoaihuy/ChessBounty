import pygame

class BoardUI():
	def __init__(self):
		self.boardMap = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
		self.pointer = 0
		display_width = 620
		display_height = 600
		self.gameDisplay = pygame.display.set_mode((display_width,display_height))
		board, self.moves = self.readBoard()
		# print(self.moves)
		self.whiteRook = pygame.transform.scale(pygame.image.load('images/white_rook.png'), (37,60))
		self.whiteKing = pygame.transform.scale(pygame.image.load('images/white_king.png'), (40,70))
		self.blackKing = pygame.transform.scale(pygame.image.load('images/black_king.png'), (40,70))
		self.wkPosi = self.getPosition(board, '11')
		self.wrPosi = self.getPosition(board, '12')
		self.bkPosi = self.getPosition(board, '21')
		self.x_white_king =  self.wkPosi[1]*72.5
		self.y_white_king = self.wkPosi[0]*72.5
		self.x_white_rook =  self.wrPosi[1]*72.5
		self.y_white_rook = self.wrPosi[0]*72.5
		self.x_black_king =  self.bkPosi[1]*72.5
		self.y_black_king = self.bkPosi[0]*72.5
		

	def readBoard(self):
		result = []
		moves = []
		with open("output.txt", "r") as f:
			lines = f.readlines()
			for i in range(0,8):
				line = lines[i].split("\t")
				line.remove("\n")
				result.append(line)
			for i in range(8,len(lines)):
				line = lines[i].split("\t")
				line[1] = line[1].split(",")

				line.remove("\n")
				moves.append(line)
		f.close
		return result, moves

	

	def getPosition(self, list, ele):
		for i1 in range(0,8):
			for i2 in range(0,8):
				if list[i1][i2] == ele:
					return [i1, i2]

		return []

	def convertMove(self, list):
		return self.boardMap[list[0]],int(list[1])-1

	def toWard(self):
		chessman = self.moves[self.pointer][0]
		pos = self.convertMove(self.moves[self.pointer][1])
		self.pointer += 1
		return chessman, pos 

	def white_rook(self,x,y):
		    self.gameDisplay.blit(self.whiteRook, (x+15,y+10))
	def white_king(self,x,y):
		    self.gameDisplay.blit(self.whiteKing, (x+15,y+4))
	def black_king(self,x,y):
		    self.gameDisplay.blit(self.blackKing, (x+15,y+4))

	def reset_game(self):
		self.white_king(self.wkPosi[1]*72.5,self.wkPosi[0]*72.5)
		self.white_rook(self.wrPosi[1]*72.5,self.wrPosi[0]*72.5)
		self.black_king(self.bkPosi[1]*72.5,self.bkPosi[0]*72.5)

	def show(self):
		pygame.init()
		
		pygame.display.set_caption('Chess Bounty')

		black = (0,0,0)
		white = (255,255,255)

		clock = pygame.time.Clock()
		crashed = False
		
		bg = pygame.image.load('images/Chessboard.jpg')

		while not crashed:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					crashed = True

		        ############################
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						if (self.pointer < len(self.moves)):
							chessman,pos = self.toWard()
							if chessman=="WK":
								self.x_white_king = pos[0]*72.5
								self.y_white_king = pos[1]*72.5
							elif chessman=="WH":
								self.x_white_rook = pos[0]*72.5
								self.y_white_rook = pos[1]*72.5
							elif chessman=="BK":
								self.x_black_king = pos[0]*72.5
								self.y_black_king = pos[1]*72.5
						
					elif event.key == pygame.K_SPACE:
						self.x_white_king =  self.wkPosi[1]*72.5
						self.y_white_king = self.wkPosi[0]*72.5
						self.x_white_rook =  self.wrPosi[1]*72.5
						self.y_white_rook = self.wrPosi[0]*72.5
						self.x_black_king =  self.bkPosi[1]*72.5
						self.y_black_king = self.bkPosi[0]*72.5
						self.pointer = 0


		        ######################
		        
			self.gameDisplay.fill(white)
			self.gameDisplay.blit(bg, (0,0))
			# gameDisplay.blit(white_rook, (x,y))
			self.white_king(self.x_white_king,self.y_white_king)
			self.white_rook(self.x_white_rook,self.y_white_rook)
			self.black_king(self.x_black_king,self.y_black_king)
		        
			pygame.display.update()
			clock.tick(60)

		pygame.quit()
		quit()