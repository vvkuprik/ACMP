text = open("INPUT.TXT", "r").readline()

n = int(text) * 100 + 90 + (9 - int(text))

file = open("OUTPUT.TXT", "w")
file.write(str(n))
file.close()