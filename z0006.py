symbol = ["A", "B", "C", "D", "E", "F", "G", "H"]
number = ["1", "2", "3", "4", "5", "6", "7", "8"]
text = open("INPUT.TXT", "r").readline()

file = open("OUTPUT.TXT", "w")
if (len(text) >= 5) and (text[0] in symbol) and (text[3] in symbol) and (text[1] in number) and (
        text[4] in number) and (text[2] == "-") and (text[0:2] != text[3:5]):

    N1 = text[0]
    D1 = text[3]

    N2 = text[1]
    D2 = text[4]

    n1 = 0
    d1 = 0

    n2 = 0
    d2 = 0

    for i in range(8):
        if N1 == symbol[i]:
            n1 = i + 1
        if D1 == symbol[i]:
            d1 = i + 1
        if N2 == number[i]:
            n2 = i + 1
        if D2 == number[i]:
            d2 = i + 1

    if (abs(n2 - d2) > 0) and (abs(n1 - d1) > 0) and (abs(n1 - d1) + abs(n2 - d2) == 3):
        file.write("YES")
    else:
        file.write("NO")
else:
    file.write("ERROR")
file.close()