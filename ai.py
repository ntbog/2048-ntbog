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
		#self.child2 = []

	def highest_tile(self):
		"""Return the highest tile here (just a suggestion, you don't have to)"""
		self.high = 0
		for i in range(4):
			for j in range(4):
				if self.high < self.tileMatrix[i][j]:
					self.high = self.tileMatrix[i][j]

		return self.high

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
		#self.treechild = []
		self.terminal = []
		
	def grow_once(self, state):
		children = []
		if state.player == 'MAX':
			for i in MOVES:
				#a = copy.deepcopy(state)
				#b = Simulator(a.tileMatrix, a.total_points)
				b = Simulator(copy.deepcopy(state.tileMatrix),state.total_points)
				#a.total_points = b.total_points
				
				#print ('before move: %d',b.total_points)
				#for j in range(0, i):
				#	b.rotateMatrixClockwise()
				#if b.canMove():
				#b.move(i)
				#print ('after move: %d',b.total_points)
				#if b.canMove():
					#print ('after move: %d',b.total_points)
				b.move(i)
				#Check if canMove in a different way
				
				if b.tileMatrix != state.tileMatrix:
				#	print ('after can move')
				#	continue
				#elif not b.canMove():
				#	continue
				#else:
				#if (self.checkequal(state.tileMatrix,a.tileMatrix)):
					#b.move(i)
					a = State(b.tileMatrix,'CHANCE',b.total_points,i)
					#a.total_points = b.total_points
					#a.pre_move = i
					#if state.player == 'MAX':
					#	a.player = 'CHANCE'
					#else:
					#	a.player = 'MAX'
					""" Line below is the problem"""
					state.child.append(a)
					children.append(a)
					#self.treechild.append(a)
					""" State is key with total_points as value"""
					#self.svdict[a] = a.total_points
					""" Child is key with Parent as value"""
					self.pdict[a] = state
					#print('Grow MAX')
			if not children:
				self.terminal.append(state)			

		else:
			for i in range(self.board_size):
					for j in range(self.board_size):
						""" Check all open chance spots"""
						if state.tileMatrix[i][j] == 0:
							""" Make copy of original state"""
							#a = copy.deepcopy(state)
							a = State(copy.deepcopy(state.tileMatrix),'MAX',state.total_points,6)
							a.tileMatrix[i][j] == 2
							#a.player = 'MAX'
							state.child.append(a)
							children.append(a)
							#self.treechild.append(a)
							self.pdict[a] = state
							#print('Grow CHANCE')
		return children

	""" Not used - check if matrix are equal, similarly used like canMove"""
	def checkequal(self,m1,m2):
		for i in range(self.board_size):
			for j in range(self.board_size):
				if m1[i][j] != m2[i][j]:
					return False
		return True

	def grow(self, state, height):
		"""Grow the full tree from root"""

		""" Another try"""
		#n = 0
		#while n < height:

		#print('in Grow')

		if height == 0:
			self.terminal.append(state)
			#state.total_points = state.total_points - 10000
			return

		else:
			#if (state.player == 'MAX'):
			children = self.grow_once(state)
				# record dictionary here
				#n = n + 1
				#height = height - 1
				#for i in state.child:
				#	self.grow(i,height)
			#else:
			#	for i in range(self.board_size):
			#		for j in range(self.board_size):
			#			""" Check all open chance spots"""
			#			if state.tileMatrix[i][j] == 0:
			#				""" Make copy of original state"""
			#				#a = copy.deepcopy(state)
			#				a = State(copy.deepcopy(state.tileMatrix),'MAX',state.total_points,6)
			#				a.tileMatrix[i][j] == 2
			#				#a.player = 'MAX'
			#				state.child.append(a)
			#				self.treechild.append(a)
			#				self.pdict[a] = state
			#				#height = height - 1
			#				#self.grow_once(a)
			#	#n = n + 1

			height = height - 1
			for i in children:
			#for i in self.treechild:
				self.grow(i,height)

	def minimax(self, state):
		"""Compute minimax values on the three"""
		""" state basically refers to the node"""
		#print('in minimax')
		if state in self.terminal:
			#print('terminal')
			#return (state.total_points+((state.highest_tile())/float(3)))
			return state.total_points + (0.3 * (state.highest_tile()))
			#return state.total_points
		elif state.player == 'MAX':
			value = float('-inf')
			#print('elif MAX player')
			for n in state.child:
				value = (max(value, self.minimax(n)))*1.0
				#self.svdict[state] = value
			self.svdict[state] = value
			#print('value from MAX ', value)
			#self.pdict[state] = state.child
			return value
		elif state.player == 'CHANCE':
			value = 0.0
			for n in state.child:
				count = len(state.child)
				if count > 0:
					value = value + self.minimax(n)*((1.0)/float(count))
			self.svdict[state] = value
			#print('value from CHANCE ', value)
			return value
		else:
			print('Error')
	def compute_decision(self):
		"""Derive a decision"""
		#Replace the following decision with what you compute
		#decision = random.randint(0,3)
		""" Instantiate the state"""
		a = State(self.root, 'MAX', 0, 4)

		#return 1
		""" Grow the tree"""
		self.grow(a, self.depth)


		myvalue = self.minimax(a)
		#print('layer 0')
		#return 2
		for key,val in self.svdict.items():
			#print('layer 1')
			if myvalue == val:
				#print('layer 2')
				""" key should hold the state with minimax value"""
		#		""" *Need logic to return the parent's child whose path is minimax"""
				#while key != a:
				#	""" v should be the child of the root whose path is minimax"""
				#	for k,v in self.pdict.items():
				#		key = k
				#		if key == a:
				#			print(MOVES[v.pre_move])
				#			return v.pre_move
				#if key == a:
				#	print('THIS SHOULD NEVER HAPPEN BEFORE')
				while key != a:
					for k,v in self.pdict.items():
						if key == k:
							key = v
						if key == a:
							print(MOVES[k.pre_move])
							return k.pre_move
				#if key == a:
				#	print('THIS SHOULD NEVER HAPPEN AFTER')
				#while key != a:
				#	print('layer3')
				#	#return 1
				#	for k,v in self.pdict.items():
				#		if key == k:
				#			key = v
				#		if key == a:
				#			print(MOVES[k.pre_move])
				#			return k.pre_move
		#print(myvalue)

		#for k,v in self.svdict.items():
		#	print('v is ', v)
		#print('myvalue is', myvalue)

		#for j in a.child:
		#	print('layer3')
		#
		#	#j.total_points = float(j.total_points)
		#	#j.total_points = 4.0
		#	print('my pre-move is ',j.pre_move)
		#	print('j.total_points', type(j.total_points), ' with value ', j.total_points)
		#	print('myvalue', type(myvalue), ' with value ', myvalue)
		#	#if True:
		#	if j.total_points == myvalue:
		#		print('layer4')
		#		print(MOVES[j.pre_move])
		#		return j.pre_move

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
		#if self.checkIfCanGo() == True:
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