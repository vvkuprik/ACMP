text = open("INPUT.TXT", "r").readline()

n = int(text) ** 2

file = open("OUTPUT.TXT", "w")
file.write(str(n))
file.close()