text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

bolt = text[0].split(" ")
gayk = text[1].split(" ")

for i in range(3):
    bolt[i] = int(bolt[i])
    gayk[i] = int(gayk[i])

otvet = bolt[0] * (bolt[1] / 100) * bolt[2] + gayk[0] * (gayk[1] / 100) * gayk[2]

ostatok1 = bolt[0] * ((100 - bolt[1]) / 100)
ostatok2 = gayk[0] * ((100 - gayk[1]) / 100)



if ostatok1 > ostatok2:
    otvet += (ostatok1 - ostatok2) * bolt[2]
elif ostatok1 < ostatok2:
    otvet += (ostatok2 - ostatok1) * gayk[2]


file = open("OUTPUT.TXT", "w")
file.write(str(int(otvet)))
file.close()

