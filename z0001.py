text = open("INPUT.TXT", "r").readline().split(" ")
file = open("OUTPUT.TXT", "w")
file.write(str(int(text[0]) + int(text[1])))
file.close()