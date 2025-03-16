text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

n = text[1].split(" ")
n.reverse()

string = ""
for i in range(len(n)):
    string += n[i]
    string += " "



file = open("OUTPUT.TXT", "w")
file.write(string)
file.close()

