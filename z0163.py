text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

n = text[0].split("=")
if n[0] == 'x':
    otvet = eval(n[1])
elif n[1] == 'x':
    otvet = eval(n[0])
elif n[0][0] == 'x':
    otvet = eval(n[1] + n[0][1] + str(int(n[0][2]) * -1))
elif n[0][2] == 'x':
    if n[0][1] == '-':
        otvet = int(eval(n[1] + n[0][1] + str(int(n[0][0])))) * -1
    else:
        otvet = eval(n[1] + n[0][1] + str(int(n[0][0]) * -1))



file = open("OUTPUT.TXT", "w")
file.write(str(int(otvet)))
file.close()

