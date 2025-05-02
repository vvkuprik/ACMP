text = open("INPUT.TXT", "r").read().split("\n")

a1 = int(text[0])
a2 = int(text[1])

file = open("OUTPUT.TXT", "w")
if a1 > a2:
    file.write(">")
elif a1 < a2:
    file.write("<")
else:
    file.write("=")
file.close()