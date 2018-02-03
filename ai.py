from __future__ import print_function
import copy, random
MOVES = {0:'up', 1:'left', 2:'down', 3:'right'}

class State:
	"""game state information"""
	#Hint: probably need the tile matrix, which player's turn, score, previous move
	def __init__(self, matrix, player, score, pre_move):
		self.tileMatrix = matrix
		self.player = player
		self.total_points = score
		self.pre_move = pre_move
		self.child = []

	def highest_tile(self):
		"""Return the highest tile here (just a suggestion, you don't have to)"""
		pass

class Gametree:
	"""main class for the AI"""
	#Hint: Two operations are important. Grow a game tree, and then compute minimax score. 
	#Hint: To grow a tree, you need to simulate the game one step. 
	#Hint: Think about the difference between your move and the computer's move. 
	def __init__(self, root, depth):
		""" root is a tileMatrix"""
		self.root = root
		""" depth - how deep to grow???"""
		self.depth = depth
		""" keep track of state with value"""
		self.svdict = {}
		""" Keep track of parenthood"""
		self.pdict = {}
		self.board_size = 4
		
	def grow_once(self, state):
#		"""Grow the tree one level deeper"""
#		""" Deep copy"""
#		a = copy.deepcopy(state)
#		a.total_points = 0
#		biggest = -1
#		
#		""" Simulate the moves. Shouldn't affect original state"""
#		""" because we explicitly make a copy"""
#		for i in MOVES:
#			b = Simulator(a.tileMatrix, a.total_points)
#			""" *Need to see if this syntax is done correctly*"""
#			if canMove():
#				b.move(i)
#				""" Initialize the state for it, unsure on PLAYER"""
#				#aa = State(b.tileMatrix,PLAYER,b.total_points,state)
#				""" Append to dictionary"""
#				#bigdict[a,aa] = aa.total_points
#
#				""" Record highest outcome"""
#				if b.total_points > biggest:
#					biggest = b.total_points
#					biggestmove = i
#
#		""" Now affect the original state"""
#		c = Simulator(state.tileMatrix, state.total_points)
#		c.move(biggestmove)
#		""" Where it came from"""
#		state.pre_move = i

		for i in MOVES:
			a = copy.deepcopy(state)
			b = Simulator(a.tileMatrix, a.total_points)
			a.total_points = b.total_points
			for j in range(0, i):
				b.rotateMatrixClockwise()
			if b.canMove():

			#b.move(i)
			#Check if canMove in a different way
			
			#if a.tileMatrix != state.tileMatrix:
			#if (self.checkequal(state.tileMatrix,a.tileMatrix)):
				a.pre_move = i
				if state.player == 'MAX':
					a.player = 'CHANCE'
				else:
					a.player = 'MAX'
				""" Line below is the problem"""
				state.child.append(a)
				""" State is key with total_points as value"""
				#self.svdict[a] = a.total_points
				""" Child is key with Parent as value"""
				self.pdict[a] = state
				print('4')
	""" Not used - check if matrix are equal, similarly used like canMove"""
	def checkequal(self,m1,m2):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if m1[i][j] != m2[i][j]:
					return False
		return True

	def grow(self, state, height):
		"""Grow the full tree from root"""
#		""" height determines type of AI: 0 = random move, 1 = depth-1 search aka grow_once, 3 = depth-3 search"""
#		#n = 0
#		#count = 0
#		biggest = -1
#		biggestmove = -1
#		#while n < height:
#		""" Max player"""
#		grow_once(state)
#		#n = n + 1
#		""" Chance player"""
#		for i in self.board_size-1:
#			for j in self.board_size-1:
#				""" Check all open chance spots"""
#				if state.tileMatrix[i][j] == 0:
#					""" Make copy of original state"""
#					a = state
#					a.tileMatrix[i][j] == 2
#					grow_once(a)
#					if (a.total_points > biggest):
#						biggest = a.total_points
#						#biggestmove = a.pre_move
#						biggesti = i
#						biggestj = j
#		state.tileMatrix[biggesti][biggestj] = 2
#		""" Max player"""
#		grow_once(state)

		""" New try"""
#		n = 0
#		if height == 1:
#			grow_once(state)
#		else:
#			while n < height:
#				grow_once(state)
#				n = n + 1
#				for i in self.board_size-1:
#					for j in self.board_size-1:
#						""" Check all open chance spots"""
#						if state.tileMatrix[i][j] == 0:
#							""" Make copy of original state"""
#							a = copy.deepcopy(state)
#							a.tileMatrix[i][j] == 2
#							grow_once(a)
#				n = n + 1
		""" Another try"""
		#n = 0
		#while n < height:

		print('in Grow')

		if height == 0:
			return

		else:
			if (state.player == 'MAX'):
				self.grow_once(state)
				# record dictionary here
				#n = n + 1
				#height = height - 1
				#for i in state.child:
				#	self.grow(i,height)
			else:
				for i in range(self.board_size):
					for j in range(self.board_size):
						""" Check all open chance spots"""
						if state.tileMatrix[i][j] == 0:
							""" Make copy of original state"""
							a = copy.deepcopy(state)
							a.tileMatrix[i][j] == 2
							a.player = 'MAX'
							state.child.append(a)
							self.pdict[a] = state
							#height = height - 1
							#self.grow_once(a)
				#n = n + 1

			height = height - 1
			for i in state.child:
				self.grow(i,height)

	def minimax(self, state):
		"""Compute minimax values on the three"""
		""" state basically refers to the node"""
		print('in minimax')
		if state.child == []:
			print('terminal')
			return state.total_points
		elif state.player == 'MAX':
			value = float('-inf')
			print('elif MAX player')
			for n in state.child:
				value = max(value, self.minimax(n))
				#self.svdict[state] = value
			self.svdict[state] = value
			#self.pdict[state] = state.child
			return value
		elif state.player == 'CHANCE':
			value = 0
			for n in state.child:
				count = 0
				for i in range(self.board_size):
					for j in range(self.board_size):
						if n.tileMatrix[i][j] == 0:
							count = count + 1
				value = value + self.minimax(n)*((1.0)/float(count))
			return value
		else:
			print('Error')
	def compute_decision(self):
		"""Derive a decision"""
		#Replace the following decision with what you compute
		#decision = random.randint(0,3)
		a = State(self.root, 'MAX', 0, 4)

		#return 1
		""" Problem line below"""
		self.grow(a, self.depth)


		myvalue = self.minimax(a)
		print('layer 0')
		#return 2
		for key,val in self.svdict.items():
			print('layer 1')
			if myvalue == val:
				print('layer 2')
				""" key should hold the state with minimax value"""
				""" *Need logic to return the parent's child whose path is minimax"""
				#while key != a:
				#	""" v should be the child of the root whose path is minimax"""
				#	for k,v in self.pdict.items():
				#		key = k
				#		if key == a:
				#			print(MOVES[v.pre_move])
				#			return v.pre_move
				while key != a:
					print('layer3')
					#return 1
					for k,v in self.pdict.items():
						if key == k:
							key = v
						if key == a:
							print(MOVES[k.pre_move])
							return k.pre_move

		print('catch')
		#return 1

						


		#Should also print the minimax value at the root
		#print(MOVES[decision])
		#return decision

class Simulator:
	"""Simulation of the game"""
	#Hint: You basically need to copy all the code from the game engine itself.
	#Hint: The GUI code from the game engine should be removed. 
	#Hint: Be very careful not to mess with the real game states. 
	def __init__(self, matrix, score):
		self.tileMatrix = matrix
		self.total_points = score
		self.board_size = 4
		
	def move(self, direction):
		#self.addToUndo()
		for i in range(0, direction):
			self.rotateMatrixClockwise()
		if self.canMove():
			self.moveTiles()
			self.mergeTiles()
			#self.placeRandomTile()
		for j in range(0, (4 - direction) % 4):
			self.rotateMatrixClockwise()
		#self.printMatrix()
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