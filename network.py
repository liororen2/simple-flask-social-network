class Network(object):
	"""docstring for Network"""
	def __init__(self):
		super(Network, self).__init__()
		self.users = []

	def getUsers(self):
		return self.users

	def addUser(self, user):
		self.users.append(user)

	def findUserById(self, id):
		print(id)
		for user in self.users:
			print(user.id)
			if user.id == int(id):
				return user


	def addConnection(self, userId1, userId2):
		user1 = self.findUserById(userId1)
		user2 = self.findUserById(userId2)
		user1.addConnection(user2)
		user2.addConnection(user1)

	def __str__(self):
		result = ""
		for u in self.users:
			result += str(u) + "\n"
		return result


