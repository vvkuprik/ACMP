text =  open("INPUT.TXT", "r").read().split("\n")

if text[-1] == "":
    del(text[-1])

komanda1 = 0
komanda2 = 0

for math in text:
    scet = math.split(" ")
    komanda1 += int(scet[0])
    komanda2 += int(scet[1])





file = open("OUTPUT.TXT", "w")
if komanda1 > komanda2:
    file.write("1")
elif komanda1 < komanda2:
    file.write("2")
else:
    file.write("DRAW")
file.close()

