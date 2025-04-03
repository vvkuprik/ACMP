text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

line0 = text[0].split()
h = int(line0[0])
w = int(line0[1])

temp = list("."*w)
MS = []
for i in range(h):
    MS.append(temp[:])

for coordinat in range (int(line0[2])):
    c = text[coordinat + 1].split()

    MS[int(c[0])-1][int(c[1])-1] = "*"

for i in range(1, len(MS)-1):
    for j in range(1, len(MS[i])-1):
        if MS[i][j] == "*":
            continue
        count = 0
        for c1 in [i-1, i ,i+1]:
            for c2 in [j-1, j, j+1]:
                if MS[c1][c2] == "*":
                    count += 1
        MS[i][j] = str(count)



if w > 1 and h > 1:

    if MS[0][0] != "*":
        count = 0
        if MS[0][1] == "*":
            count += 1
        if MS[1][1] == "*":
            count += 1
        if MS[1][0] == "*":
            count += 1
        MS[0][0] = str(count)

    if MS[0][-1] != "*":
        count = 0
        if MS[0][-2] == "*":
            count += 1
        if MS[1][-1] == "*":
            count += 1
        if MS[1][-2] == "*":
            count += 1
        MS[0][-1] = str(count)

    if MS[-1][-1] != "*":
        count = 0
        if MS[-1][-2] == "*":
            count += 1
        if MS[-2][-2] == "*":
            count += 1
        if MS[-2][-1] == "*":
            count += 1
        MS[-1][-1] = str(count)

    if MS[-1][0] != "*":
        count = 0
        if MS[-2][0] == "*":
            count += 1
        if MS[-2][1] == "*":
            count += 1
        if MS[-1][1] == "*":
            count += 1
        MS[-1][0] = str(count)

    for j in range(1, len(MS[0]) - 1):
        if MS[0][j] == "*":
            continue
        count = 0
        if MS[0][j - 1] == "*":
            count += 1
        if MS[0][j + 1] == "*":
            count += 1
        if MS[1][j - 1] == "*":
            count += 1
        if MS[1][j] == "*":
            count += 1
        if MS[1][j + 1] == "*":
            count += 1
        MS[0][j] = str(count)

    for j in range(1, len(MS[-1]) - 1):
        if MS[-1][j] == "*":
            continue
        count = 0
        if MS[-1][j - 1] == "*":
            count += 1
        if MS[-1][j + 1] == "*":
            count += 1
        if MS[-2][j - 1] == "*":
            count += 1
        if MS[-2][j] == "*":
            count += 1
        if MS[-2][j + 1] == "*":
            count += 1
        MS[-1][j] = str(count)

    for i in range(1, len(MS) - 1):
        if MS[i][0] == "*":
            continue
        count = 0
        if MS[i - 1][0] == "*":
            count += 1
        if MS[i + 1][0] == "*":
            count += 1
        if MS[i - 1][1] == "*":
            count += 1
        if MS[i][1] == "*":
            count += 1
        if MS[i + 1][1] == "*":
            count += 1
        MS[i][0] = str(count)

    for i in range(1, len(MS) - 1):
        if MS[i][-1] == "*":
            continue
        count = 0
        if MS[i - 1][-1] == "*":
            count += 1
        if MS[i + 1][-1] == "*":
            count += 1
        if MS[i - 1][-2] == "*":
            count += 1
        if MS[i][-2] == "*":
            count += 1
        if MS[i + 1][-2] == "*":
            count += 1
        MS[i][-1] = str(count)
elif w == 1 and h > 1:
    for j in range(len(MS)):
        if MS[j][0] == "*":
            continue
        elif j == 0:
            if MS[j+1][0] == "*":
                MS[j][0] = "1"
        elif j == len(MS) - 1:
            if MS[j-1][0] == "*":
                MS[j][0] = "1"
        else:
            count = 0
            if MS[j+1][0] == "*":
                count += 1
            if MS[j-1][0] == "*":
                count += 1
            MS[j][0] = str(count)
elif h == 1 and w > 1:
    for i in range(len(MS[0])):
        if MS[0][i] == "*":
            continue
        elif i == 0:
            if MS[0][i+1] == "*":
                MS[0][i] = "1"
        elif i == len(MS[0]) - 1:
            if MS[0][i-1] == "*":
                MS[0][i] = "1"
        else:
            count = 0
            if MS[0][i+1] == "*":
                count += 1
            if MS[0][i-1] == "*":
                count += 1
            MS[0][i] = str(count)

file = open("OUTPUT.TXT", "w")
for i in range(len(MS)):
    for j in range(len(MS[i])):
        if MS[i][j] != "0":
            file.write(MS[i][j])
        else:
            file.write(".")
    file.write("\n")

file.close()

