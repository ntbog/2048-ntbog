from __future__ import print_function
import copy, random
MOVES = {0:'up', 1:'left', 2:'down', 3:'right'}

class State:
	"""game state information"""
	#Hint: probably need the tile matrix, which player's turn, score, previous move
	def __init__(self, matrix, player, score, pre_move):
		self.matrix = matrix
		self.player = player
		self.score = score
		self.pre_move = pre_move

		
	def highest_tile(self):
		"""Return the highest tile here (just a suggestion, you don't have to)"""
		pass

class Gametree:
	"""main class for the AI"""
	#Hint: Two operations are important. Grow a game tree, and then compute minimax score. 
	#Hint: To grow a tree, you need to simulate the game one step. 
	#Hint: Think about the difference between your move and the computer's move. 
	def __init__(self, root, depth):
		pass
	def grow_once(self, state):
		"""Grow the tree one level deeper"""
		pass
	def grow(self, state, height):
		"""Grow the full tree from root"""
		pass
	def minimax(self, state):
		"""Compute minimax values on the three"""
		pass
	def compute_decision(self):
		"""Derive a decision"""
		#Replace the following decision with what you compute
		decision = random.randint(0,3)
		#Should also print the minimax value at the root
		print(MOVES[decision])
		return decision

class Simulator:
	"""Simulation of the game"""
	#Hint: You basically need to copy all the code from the game engine itself.
	#Hint: The GUI code from the game engine should be removed. 
	#Hint: Be very careful not to mess with the real game states. 
	def __init__(self, matrix, score):
		pass
	def move(self, direction):
		pass
	def moveTiles(self):
		tm = self.tileMatrix
		for i in range(0, self.board_size):
			for j in range(0, self.board_size - 1):
				while tm[i][j] == 0 and sum(tm[i][j:]) > 0:
					for k in range(j, self.board_size - 1):
						tm[i][k] = tm[i][k + 1]
					tm[i][self.board_size - 1] = 0
		
	def mergeTiles(self):
		tm = self.tileMatrix
		for i in range(0, self.board_size):
			for k in range(0, self.board_size - 1):
				if tm[i][k] == tm[i][k + 1] and tm[i][k] != 0:
					tm[i][k] = tm[i][k] * 2
					tm[i][k + 1] = 0
					self.total_points += tm[i][k]
					self.moveTiles()
		
	def checkIfCanGo(self):
		tm = self.tileMatrix
		for i in range(0, self.board_size ** 2):
			if tm[int(i / self.board_size)][i % self.board_size] == 0:
				return True		
		for i in range(0, self.board_size):
			for j in range(0, self.board_size - 1):
				if tm[i][j] == tm[i][j + 1]:
					return True
				elif tm[j][i] == tm[j + 1][i]:
					return True
		return False
		
	def canMove(self):
		tm = self.tileMatrix
		for i in range(0, self.board_size):
			for j in range(1, self.board_size):
				if tm[i][j-1] == 0 and tm[i][j] > 0:
					return True
				elif (tm[i][j-1] == tm[i][j]) and tm[i][j-1] != 0:
					return True
		return False
		
	def rotateMatrixClockwise(self):	
		tm = self.tileMatrix
		for i in range(0, int(self.board_size/2)):
			for k in range(i, self.board_size- i - 1):
				temp1 = tm[i][k]
				temp2 = tm[self.board_size - 1 - k][i]
				temp3 = tm[self.board_size - 1 - i][self.board_size - 1 - k]
				temp4 = tm[k][self.board_size - 1 - i]
				tm[self.board_size - 1 - k][i] = temp1
				tm[self.board_size - 1 - i][self.board_size - 1 - k] = temp2
				tm[k][self.board_size - 1 - i] = temp3
				tm[i][k] = temp4	
	def convertToLinearMatrix(self):
		m = []
		for i in range(0, self.board_size ** 2):
			m.append(self.tileMatrix[int(i / self.board_size)][i % self.board_size])
		m.append(self.total_points)
		return m
		
