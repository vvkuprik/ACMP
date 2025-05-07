text = open("INPUT.TXT", "r").read().split("\n")

k = int(text[0])
ms = []
for i in text[1].split():
    if i != "":
        ms.append(int(i))

otvet = 0
if k == 1:
    otvet = ms[0] // 2 + 1
else:
    ms.sort()
    for i in range(k//2+1):
        otvet += ms[i] // 2 + 1


file =open("OUTPUT.TXT", "w")
file.write(str(otvet))
file.close()

