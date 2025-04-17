text = open("INPUT.TXT", "r").read().split("\n")[1]

MS = [int(i) for i in text.split()]


MX = 0
temp_i = MS[0]

for i in set(MS):
    cnt = MS.count(i)
    if MX < cnt:
        MX = cnt
        temp_i = i
    elif MX == cnt:
        if i < temp_i:
            temp_i = i


cnt = 0
i = 0
while i < len(MS) :
    if MS[i] == temp_i:
        cnt += 1
        del(MS[i])
        continue

    i += 1

for i in range(cnt):
    MS.append(temp_i)

file = open("OUTPUT.TXT", "w")
ot = " ".join(str(i) for i in MS)
file.write(ot)
file.close()


