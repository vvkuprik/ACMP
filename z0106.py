text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

count = int(text[0])
del(text[0])
counter0 = 0
counter1 = 0
for i in range(count):
    if text[i] == '0':
        counter0 += 1
    elif text[i] == '1':
        counter1 += 1


file = open("OUTPUT.TXT", "w")
file.write(str(min(counter0, counter1)))
file.close()

