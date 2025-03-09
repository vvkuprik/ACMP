text = open("INPUT.TXT", "r").read().split("\n")

ms1 = set([int(i) for i in text[1].split()])
ms2 = set([int(i) for i in text[2].split()])

ot = list(ms1 & ms2)


ot.sort()

s = " ".join([str(i) for i in ot])

file = open("OUTPUT.TXT", "w")
file.write(s)
file.close()

