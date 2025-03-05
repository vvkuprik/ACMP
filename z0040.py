text =  open("INPUT.TXT", "r").read().split("\n")[0].split(" ")

N = int(text[0])

otvet = str(2 ** N)


file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

