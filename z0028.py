text =  open("INPUT.TXT", "r").read().split("\n")

line = text[0].split(" ")
dot = text[1].split(" ")



if (int(line[0]) == int(line[2]) == 0) or (int(line[1]) == int(line[3]) == 0):
    if line[0] == line[2]:
        if line[0] != dot[0]:
            dot[0] = str(int(dot[0]) * -1)

    elif line[1] == line[3]:
        if line[1] != dot[1]:
            dot[1] = str(int(dot[1]) * -1)
else:
    if line[0] == line[2]:
        if line[0] != dot[0]:
            dot[0] = str(int(line[0]) - (int(dot[0]) - int(line[0])))

    elif line[1] == line[3]:
        if line[1] != dot[1]:
            dot[1] = str(int(line[1]) - (int(dot[1]) - int(line[1])))



file = open("OUTPUT.TXT", "w")
file.write(dot[0] + " " + dot[1])
file.close()
