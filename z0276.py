text =  open("INPUT.TXT", "r").read().split("\n")
n = int(text[0].split(" ")[0])
m = int(text[0].split(" ")[1])


otvet = ""
if n%m == 0:
    otvet = (str(n//m) + " ") * m

else:
    MS = []
    for i in range(m):
        MS.append(n//m)

    print((n//m) + 1)
    MS.reverse()
    for i in range(n%m):
        MS[i] += 1

    MS.reverse()

    for i in range(len(MS)):
        otvet += str(MS[i])
        otvet += " "



file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

