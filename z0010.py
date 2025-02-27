text =  open("INPUT.TXT", "r").readline().split("\n")[0].split(" ")
A = int(text[0])
B = int(text[1])
C = int(text[2])
D = int(text[3])

otvel = ""
for i in range(-100, 101):
    if (A * (i**3) + B * (i**2) + C * i + D) == 0:
        otvel += str(i) + " "

file = open("OUTPUT.TXT", "w")
file.write(otvel)
file.close()
