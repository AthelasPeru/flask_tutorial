# -*- coding: utf-8 -*-

def main():
	try:
		size = int(raw_input("Cual es el largo de tu nepe? "))
		comparado = int(raw_input("Cual es el largo del nepe que te atemoriza? "))
	except ValueError:
		print "Ese no es un tamaño de nepe real\n"
		main()
		
	if size> comparado:
		print "Haste ver, tu nepe es mas grande\n"
	elif size < comparado:
		print "Tendras que esforzarte, quiza debes pedir consejo a Polo\n"
	elif size == comparado:
		print "Son iguales, estas cagadoo, a la primera se confnde y te cambia\n"
	seguir = raw_input("Deseas compararte de nuevo?(Yy/Nn)")
	if seguir not in "yYnN":
		print "lo siento, eres un bruto y apretaste otra vaina, se acabó para ti\n"
	else:
		if seguir in "yY":
			main()
		else:
			print "Adios amigo\n"


if __name__ == '__main__':
	main()