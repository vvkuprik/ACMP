text = open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

misheni = [[0, 0], [25, 0], [50, 0], [75, 0], [100, 0]]

for i in range(5):
    vXY = text[i].split()
    vX = int(vXY[0])
    vY = int(vXY[1])
    for j in range(len(misheni)):
        if ((vX - misheni[j][0]) ** 2 + (vY - misheni[j][1]) ** 2) ** 0.5 <= 10:
            del(misheni[j])
            break


file = open("OUTPUT.TXT", "w")
file.write(str(5 - len(misheni)))
file.close()

