text =  open("INPUT.TXT", "r").read().split("\n")
text = text[0].split(" ")


file = open("OUTPUT.TXT", "w")
if int(text[0]) * int(text[1]) == int(text[2]):
    file.write("YES")
else:
    file.write("NO")
file.close()
