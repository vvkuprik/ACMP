text = open("INPUT.TXT", "r").read().split("\n")[0].split()

n = int(text[0])
k = int(text[1])

MS = []

for i in range(1, n+1):
    MS.append(str(i))

MS.sort()



open("OUTPUT.TXT", "w").write(str(MS.index(str(k))+1))


