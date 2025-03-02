def test(x1, y1, x2, y2):
    global MS
    for i in range(y1, y2):
        MS[i] = MS[i][:x1] + "1"*(x2-x1) + MS[i][x2:]

text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])
Str = text[0].split()
w = int(Str[0])
h = int(Str[1])

MS = []
for i in range(h):
    MS.append("0"*w)

for coordinat in range (2, len(text)):
    c = text[coordinat].split()
    test(int(c[0]), int(c[1]), int(c[2]), int(c[3]))


count = 0
for line in MS:
    count += line.count("0")


file = open("OUTPUT.TXT", "w")

file.write(str(count))
file.close()

