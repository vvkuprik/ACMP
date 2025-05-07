colorList = [".", ".B", ".G", ".GB", ".R", ".RB", ".RG", '.RGB']

def testing():
    for i in range(n):
        for j in range(m):
            if smsList[i][j] not in colorList[int(tableList[i][j])]:
                return "NO"
    return "YES"

text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

n = int(text[0].split()[0])
m = int(text[0].split()[1])
del(text[0])

smsList = []
tableList = []

for i in range(n):
    smsList.append(list(text[0]))
    tableList.append(text[n].split())
    del(text[0])

otvet = testing()

file = open("OUTPUT.TXT", "w")
file.write(otvet)

file.close()

