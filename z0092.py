text =  open("INPUT.TXT", "r").read().split("\n")


children = int(text[0])
part = children // 6
print(part)

file = open("OUTPUT.TXT", "w")
file.write(str(part) + " " + str(part*4) + " " + str(part))
file.close()

