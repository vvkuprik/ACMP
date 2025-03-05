def scet(n, m):
    return str(19 * m + (n + 239) * (n + 366) // 2)


text =  open("INPUT.TXT", "r").read().split("\n")

file = open("OUTPUT.TXT", "w")

for i in range(1, int(text[0])+1):
    nm = text[i].split(" ")
    file.write(scet(int(nm[0]), int(nm[1])) + "\n")

file.close()

