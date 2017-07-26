from flask import Flask
from flask import render_template
from user import User
from network import Network

# from flask import request
app = Flask(__name__)


a = User("Sarah")
b = User("Katie")
n = Network()
n.addUser(a)
n.addUser(b)
n.addConnection(0,1)
print(n)
print(a)
print(a.getConnections())

@app.route("/")
def index():
	return render_template('index.html', users=n.getUsers())

@app.route("/users/<user_id>")
def user(user_id):
	user = n.findUserById(user_id)
	print(user)
	connections = user.getConnections()
	print(connections)
	return render_template('user.html', user=user, connections=connections)


