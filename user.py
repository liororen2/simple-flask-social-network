class User(object):
	nextId = 0
	"""docstring for User"""
	def __init__(self, name):
		super(User, self).__init__()
		self.name = name
		self.id = User.nextId
		self.connections = []
		User.nextId += 1

	def addConnection(self, otherUser):
		self.connections.append(otherUser)

	def getConnections(self):
		return self.connections

	def __str__(self):
		return self.name + " " + str(self.id)