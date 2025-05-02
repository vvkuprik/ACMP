text = open("INPUT.TXT", "r").read().split("\n")
count0 = int(text[0])

ms = []
for i in text[1].split():
    if i != '':
        ms.append(int(i))

ind = ms.index(min(ms))
ms = ms[ind:] + ms[:ind]

file = open("OUTPUT.TXT", "w")
for i in ms:
    file.write(str(i) + " ")

file.close()
