symbols1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

text = open("INPUT.TXT", "r").read().split("\n")[0]

symbols2 = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , ' ']

#for i in range(len(text)):
#    print(symbols1[symbols2.index(text[i]) + i + 1])


otvet = ""
for i in range(len(text)):
    otvet += symbols2[(symbols1.index(text[i]) - 1 - i) % 27]


open("OUTPUT.TXT", 'w').write(otvet)

