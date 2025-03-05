text =  open("INPUT.TXT", "r").readline().split("\n")[0]
hvost = [7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9, 0, 4, 5, 2, 3, 5, 3, 6, 0, 2, 8, 7, 5]

otvet = "2."
if text == "0":
    otvet = "3"
elif text == "25":
    for i in hvost:
        otvet += str(i)
else:
    if hvost[int(text)] > 4:
        hvost[int(text) - 1] += 1
    for i in range(int(text)):
        otvet += str(hvost[i])


file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

