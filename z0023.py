text =  open("INPUT.TXT", "r").read().split("\n")
number = int(text[0])

summ = 0

for i in range(1, number+1):
    if number % i == 0:
        summ += i

file = open("OUTPUT.TXT", "w")
file.write(str(summ))
file.close()

