import itertools
text = open("INPUT.TXT", 'r').read().split("\n")

a = "+-"
n = int(text[0].split()[0])

if n > 1:
    otvet = text[0].split()[1]
    varianty = set(itertools.permutations(a*n, n-1))
    numbers = text[1].split()

    file = open("OUTPUT.TXT", "w")

    for znaki in varianty:
        primer = ""
        for i in range(n-1):
            primer += numbers[i] + znaki[i]
        primer += numbers[i+1]
        if eval(primer + "==" + otvet):
            file.write(primer + "=" + otvet)
            break
    else:
        file.write("No solution")
    file.close()

else:
    otvet = int(text[0].split()[1])
    numbers = int(text[1])
    file = open("OUTPUT.TXT", "w")
    if otvet == numbers:
        file.write(str(numbers) + "=" + str(otvet))
    else:
        file.write("No solution")
    file.close()
