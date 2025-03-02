text =  open("INPUT.TXT", "r").read().split("\n")
number = text[0].split(" ")
banok = int(number[0]) + int(number[1]) - 1
s = str(banok - int(number[0])) + " " + str(banok - int(number[1]))
file = open("OUTPUT.TXT", "w")
file.write(s)
file.close()

