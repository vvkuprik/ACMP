symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def perevod(number, scet):
    if len(str(scet)) == 1:
        sistem = symbols.index(str(scet))
    else:
        sistem = int(scet)

    new_number = []
    while number / sistem >= 1:
        new_number.append(symbols[number % sistem])
        number //= sistem
    new_number.append(symbols[number])

    returnNumber = ""
    for i in range(len(new_number)-1, -1, -1):
        returnNumber += str(new_number[i])

    return returnNumber



text =  open("INPUT.TXT", "r").read().split("\n")
n = int(text[0])

otvet = []

for i in range(2, 37):
    new_n = perevod(n, i)
    if new_n == new_n[::-1]:
        otvet.append(str(i))







file = open("OUTPUT.TXT", "w")

if len(otvet) == 0:
    file.write("none")
elif len(otvet) == 1:
    file.write("unique\n")
    file.write(otvet[0])
else:
    file.write("multiple\n")
    for i in otvet:
        file.write(i + " ")
file.close()

