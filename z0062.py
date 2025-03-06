symbol = ["A", "B", "C", "D", "E", "F", "G", "H"]
number = ["1", "2", "3", "4", "5", "6", "7", "8"]


file = open("INPUT.TXT", "r")
s = file.read(1)
n = file.read(1)
file.close()

countS = symbol.index(s)
countN = number.index(n)

file = open("OUTPUT.TXT", "w")
if (countS + countN) % 2 == 0:
    file.write("BLACK")
else:
    file.write("WHITE")
file.close()
