def test(ms):
    global otvet
    c = 0
    for i in range(len(ms)-1):
        for j in range(len(ms[i])-1):
            if ms[i][j] == ms[i+1][j] == ms[i][j+1] == ms[i+1][j+1]:
                otvet += "NO\n"
                return
    if c == 0:
        otvet += "YES\n"


text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])



otvet = ""
countTest = int(text[0])
del(text[0])

for i in range(countTest):
    n = int(text[0].split()[0])
    m = int(text[0].split()[1])
    del(text[0])
    if n < 2 or m < 2:
        otvet += "YES\n"
        for i in range(n):
            del(text[0])
    else:
        ms = []
        for i in range(n):
            ms.append(text[0].split())
            del(text[0])
        test(ms)

file = open("OUTPUT.TXT", "w")
file.write(otvet)

file.close()

