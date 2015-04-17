def main():
	size = raw_input("Cual es el largo de tu nepe?")
	comparado = raw_input("Cual es el largo del nepe que te atemoriza?")
	if type(size) not in [int, float]:
		print "Ese no es un tamaño de nepe real"
		main()
	elif size > comparado:
		print "Haste ver, tu nepe es más grande"
	elif size < comparado:
		print "Tendras que esforzarte, quizá debes pedir consejo a Polo"

	seguir = raw_input("Deseas compararte de nuevo?(Yy/Nn)")
	if seguir not in ["yYnN"]:
		print "lo siento, eres un bruto y apretaste otra vaina, se acabó para tí"
	else:
		if seguir in ["yY"]:
			main()
		else:
			print "Adios amigo"


if __name__ == '__main__':
	main()