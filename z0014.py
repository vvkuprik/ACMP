text =  open("INPUT.TXT", "r").read().split("\n")[0].split(" ")

a = int(text[0])
b = int(text[1])

def test(a, b):
    n = max(a, b) % min(a, b)
    otvet = min(a, b)
    i = 0

    while True:
        if n > 0:
            otvet = n
        if b % otvet == 0 and a % otvet == 0:
            break

        if i%2 == 0 and min(a, b) % n > 0:
            n = min(a, b) % n
        elif i%2 == 1 and max(a, b) % n > 0:
            n = max(a, b) % n
        i+=1

    NOK = a * b // otvet
    file.write(str(NOK))




file = open("OUTPUT.TXT", "w")
test(a, b)
file.close()

