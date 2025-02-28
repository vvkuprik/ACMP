text =  open("INPUT.TXT", "r").read().split("\n")
number = int(text[0])

number = bin(number)[2:]
count = 0
for i in number:
    if i == "1":
        count += 1

file = open("OUTPUT.TXT", "w")
file.write(str(count))
file.close()

