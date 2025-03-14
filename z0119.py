text =  open("INPUT.TXT", "r").read().split("\n")

if text[-1] == "":
    del(text[-1])



n = int(text[0])
del(text[0])

timeList = []
secondList = []

for i in range(n):
    timeList.append(text[0].split())
    secondList.append(int(timeList[-1][0]) * 3600 + int(timeList[-1][1]) * 60 + int(timeList[-1][2]))
    del(text[0])

tempList = secondList[:]
secondList.sort()

otvet = ""
for i in secondList:
    for j in timeList[tempList.index(i)]:
        otvet += str(int(j)) + " "
    otvet += "\n"

file = open("OUTPUT.TXT", "w")
file.write(otvet)

file.close()

