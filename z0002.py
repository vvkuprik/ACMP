text = open("INPUT.TXT", "r").readline()

n = int(text)
s = 0

for i in range(1, n + 1):
    s += i
for i in range(n, 2):
    s += i

file = open("OUTPUT.TXT", "w")
file.write(str(s))
file.close()