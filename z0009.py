text =  open("INPUT.TXT", "r").read().split("\n")
n = int(text[0])
numer = text[1].split(" ")

s = 0


for i in range(n):
    numer[i] = int(numer[i])
    if numer[i] > 0:
        s += numer[i]

mn = numer.index(min(numer))
mx = numer.index(max(numer))



p = 1
for i in range(mn+1, mx):
    p *= numer[i]
for i in range(mx+1, mn):
    p *= numer[i]


file = open("OUTPUT.TXT", "w")
file.write(str(s) + " " + str(p))
file.close()
