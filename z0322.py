
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]
print(len(fib))
text = open("INPUT.TXT", "r").read().split("\n")[0]

otvet = ""

for i in range(len(text)):
    if i+1 in fib:
        otvet += text[i]

file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()
