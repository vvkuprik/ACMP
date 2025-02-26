text = open("INPUT.TXT", "r").read().split("\n")
n = int(text[0])
days = text[1].split(" ")

cet = []
noCet = []

for i in range(n):
    if int(days[i]) % 2 == 1:
        noCet.append(days[i])
    else:
        cet.append(days[i])

n1 = len(noCet)
n2 = len(cet)

file = open("OUTPUT.TXT", "w")
for i in noCet:
    file.write(i + " ")
file.write("\n")

for i in cet:
    file.write(i + " ")
file.write("\n")

if n1 > n2:
    file.write("NO")
else:
    file.write("YES")

file.close()