from __future__ import print_function

def reconocer(item):
	"""
	param: item -> cualquier item que qieras biatc
	"""

	if type(item) is str:
		print("It's a string")
	elif type(item) is int:
		print("It's an integer")
	elif type(item) == "function":
		print("Its a function")
	else: 
		print("I don't know what it is")


lista = [2,3,4,5,6,7]
_tuple =(2,3,4,5,6,7)
diccionario = {"player1":"pedro", "player2": 2, "player3": lista, "player4": reconocer}


