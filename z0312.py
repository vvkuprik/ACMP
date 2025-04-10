text =  open("INPUT.TXT", "r").read().split("\n")
a1 = int(text[0].split(" ")[0])
a2 = int(text[0].split(" ")[1])
n = int(text[0].split(" ")[2])

otvet = (a2 - a1) * (n - 1) + a1


file = open("OUTPUT.TXT", "w")
file.write(str(otvet))
file.close()

