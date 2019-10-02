# -*- coding: utf-8 -*- 

KEYS = {
	"a": "01100001",
	"b": "01100010",
	"c": "01100011",
	"d": "01100100",
	"e": "01100101",
	"f": "01100110",
	"g": "01100111",
	"h": "01101000",
	"i": "01101001",
	"j": "01101010",
	"k": "01101011",
	"l": "01101100",
	"m": "01101101",
	"n": "01101110",
	"o": "01101111",
	"p": "01110000",
	"q": "01110001",
	"r": "01110010",
	"s": "01110011",
	"t": "01110100",
	"u": "01110101",
	"v": "01110110",
	"w": "01110111",
	"x": "01111000",
	"y": "01111001",
	"z": "01111010"
}

def cypher(message):
	words = message.split(" ")
	cypher_message = []

	for word in words:
		cypher_word = " "
		for letter in word:
			cypher_word += KEYS[letter]

		cypher_message.append(cypher_word)

	return " ".join(cypher_message)

def decipher(message):
	words = message.split(" ")
	decipher_message = []

	for word in words:
		decipher_word = " "

		for letter in word: 

			for key, value in KEYS.iteritems():
				if value == letter:
					decipher_word += key

		decipher_message.append(decipher_word)

	return " ".join(decipher_message)


def run():
	

	while True:

		command = str(input("""---*---*---*---*---*---*---*
		Bienvenido a criptografía. ¿Qué deseas hacer?

		[c]ifrar mensaje
		[d]ecifrar mensaje
		[s]alir
		"""))

		if command == "c":
			message =str(input("Escribe tu mensaje: "))
			cypher_message = cypher(message)
			print(cypher_message)

		elif command == "d":
			  message =str(input("Escribe tu mensaje cifrado:  "))
			  decypher_message = decipher(message)
			  print(decypher_message)
		
		elif command == "s":
			print("salir")
		else:
			print("comando no encontrado")



if __name__ == "__main__":
	print("M E N S A J E S  C I F R A D O S")
	run()








