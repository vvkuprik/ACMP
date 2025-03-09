text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])


arbuz = text[1].split(" ")
for i in range(int(text[0])):
    arbuz[i] = int(arbuz[i])

otvet = str(min(arbuz)) + " " + str(max(arbuz))

file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

