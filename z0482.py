text =  open("INPUT.TXT", "r").read().split("\n")[0].split()[0]

s = ""
for i in range(1, 32768):
    for j in range(1, i):
        s += str(j)
    if len(s) > 32768:
        break

n = int(text)


file = open("OUTPUT.TXT", "w")
file.write(str(s[n-1]))
file.close()

