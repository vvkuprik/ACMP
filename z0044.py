text =  open("INPUT.TXT", "r").read().split("\n")

arows = text[0]

ar1 = ">>-->"
ar2 = "<--<<"

count = 0

for i in range(len(arows)-4):
    if arows[i:i+5] == ar1 or arows[i:i+5] == ar2:
        count += 1

file = open("OUTPUT.TXT", "w")
file.write(str(count))
file.close()

