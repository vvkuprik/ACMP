text =  open("INPUT.TXT", "r").readline()
#namber = text[0]
summ = []

s = 0
for i in text:
    if i == "\n":
        break
    if i == "0":
        s += 1
    else:
        summ.append(s)
        s = 0
summ.append(s)
file = open("OUTPUT.TXT", "w")
file.write(str(max(summ)))
file.close()

