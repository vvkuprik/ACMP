symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def returnPerevod(number, scet):
    if len(str(scet)) == 1:
        sistem = symbols.index(str(scet))
    else:
        sistem = scet

    number = str(number)
    new_number = 0
    for i in range(len(number)):
        new_number += symbols.index(number[-1-i]) * (sistem ** i)

    return new_number



text =  open("INPUT.TXT", "r").read().split("\n")
n = int(text[0])
n = bin(n)[2:]
spisok = []


for i in range(len(n)):
    spisok.append(n[i:] + n[:i])


n = returnPerevod(max(spisok), 2)

file = open("OUTPUT.TXT", "w")
file.write(str(n))
file.close()

