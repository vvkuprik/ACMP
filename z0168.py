text =  open("INPUT.TXT", "r").read().split("\n")[0]


string = ""
counter = 1
while True:
    string += str(counter)
    if text in string:
        counter = len(string.split(text)[0]) + 1
        break
    counter += 1



file = open("OUTPUT.TXT", "w")
file.write(str(counter))
file.close()

