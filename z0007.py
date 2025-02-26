text = open("INPUT.TXT", "r").read().split("\n")
text = text[0].split(" ")

print(text)
otvet = 0
for i in range(len(text)):
    if int(text[i]) > otvet:
        otvet = int(text[i])

file = open("OUTPUT.TXT", "w")
file.write(str(otvet))
file.close()