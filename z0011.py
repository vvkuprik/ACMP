text =  open("INPUT.TXT", "r").readline().split("\n")[0].split(" ")
k = int(text[0])
n = int(text[1])

fibanaci = [1, 1]
for i in range(2, n + 1):
    s = 0
    for j in range(len(fibanaci) - min(k, len(fibanaci)),  len(fibanaci)):
        s += fibanaci[j]
    fibanaci.append(s)
print(fibanaci)

file = open("OUTPUT.TXT", "w")
file.write(str(fibanaci[n]))
file.close()
