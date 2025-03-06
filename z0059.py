symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def perevod(number, scet):
    if len(str(scet)) == 1:
        sistem = symbols.index(str(scet))
    else:
        sistem = scet

    new_number = []
    while number / sistem > 1:
        new_number.append(str(number % sistem))
        number //= sistem
    new_number.append(str(number))

    returnNumber = ""
    for i in range(len(new_number)-1, -1, -1):
        returnNumber += str(new_number[i])

    return returnNumber


text =  open("INPUT.TXT", "r").read().split("\n")

number1 = int(text[0].split(" ")[0])
number2 = int(text[0].split(" ")[1])


if number2 != 10:
    number1 = perevod(number1, number2)

count1 = 1
count2 = 0

for i in str(number1):
    count1 *= int(i)
    count2 += int(i)

file = open("OUTPUT.TXT", "w")
file.write(str(count1 - count2))
file.close()

