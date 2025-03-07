text = open("INPUT.TXT", "r").read().split("\n")

Sum = int(text[0].split(" ")[0])
Mul = int(text[0].split(" ")[1])

count1 = -1
count2 = -1
for i in range(1, 1001):
    for j in range(1, 1001):
        if (i + j) == Sum and (i * j) == Mul:
            count1 = i
            count2 = j


file = open("OUTPUT.TXT", "w")
file.write(str(min(count1, count2)) + " " + str(max(count1, count2)))
file.close()
