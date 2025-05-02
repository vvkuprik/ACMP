
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


    return otvet

text = open("INPUT.TXT", "r").read().split("\n")[0].split()


fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903]

F1 = fib[int(text[0])]
F2 = fib[int(text[1])]
print(F1)
print(F2)
n = test(F1, F2)


file = open("OUTPUT.TXT", "w")
file.write(str(n))
file.close()

