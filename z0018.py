text =  open("INPUT.TXT", "r").read().split("\n")[0].split(" ")

N = int(text[0])
if N == 0:
    otvet = "1"
elif N == 1:
    otvet = "1"
else:
    otvet = 1
    for i in range(2, N+1):
        otvet *= i
    otvet = str(otvet)


file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

