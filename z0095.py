text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])


number = text[0]
counter = 0

if len(number) == 1:
    numberSUMM = int(number[0])


while len(number) > 1:
    counter += 1
    numberSUMM = int(number[0])
    for i in range(1, len(number)):
        numberSUMM += int(number[i])

    number = str(numberSUMM)


file = open("OUTPUT.TXT", "w")
file.write(number + " " + str(counter))
file.close()

