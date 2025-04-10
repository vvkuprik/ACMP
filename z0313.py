text = open("INPUT.TXT", "r").read().split("\n")

n = int(text[0])
bus = []
for number in text[1].split():
    if number.isdigit():
        bus.append(int(number))

maxx = 0

if len(bus) == len(set(bus)) + 1:
    maxx = 1
else:
    for i in range(len(bus)):
        count = 0
        for j in range(i + 1, len(bus)):
            if bus[i] == bus[j]:
                count = j - i
                break
        if count > maxx:
            maxx = count



open("OUTPUT.TXT", "w").write(str(maxx))


