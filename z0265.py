text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

MS = []
for i in range(8):
    MS.append(list("0"*8))

for i in range(1, 1 + int(text[0])):
    coord = text[i].split()
    MS[int(coord[0]) - 1][int(coord[1]) - 1] = "#"

count = 0

for i in range(len(MS)):
    for j in range(len(MS[i])):
        if MS[i][j] == "#":

            if j == len(MS[0])-1:
                count += 1
            elif MS[i][j+1] != "#" and j < len(MS[i])-1:
                count += 1

            if j == 0:
                count += 1
            elif MS[i][j-1] != "#" and j > 0:
                count += 1

            if i == 0:
                count += 1
            elif MS[i-1][j] != "#" and i > 0:
                count += 1

            if i == len(MS)-1:
                count += 1
            elif MS[i+1][j] != "#" and i < len(MS)-1:
                count += 1





file = open("OUTPUT.TXT", "w")
file.write(str(count))

file.close()

