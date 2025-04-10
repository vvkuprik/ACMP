symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]





text =  open("INPUT.TXT", "r").read().split("\n")[0]

otvet = -1

for symbol in text:
    if symbol in symbols:
        sistem = symbols.index(symbol)
        if sistem >= otvet:
            otvet = sistem + 1
    else:
        otvet = -1
        break

if text.isdigit():
    if int(text) < 2:
        otvet = 2

file = open("OUTPUT.TXT", "w")
file.write(str(otvet))
file.close()

