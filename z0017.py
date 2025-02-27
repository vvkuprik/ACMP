text =  open("INPUT.TXT", "r").read().split("\n")[1].split(" ")
print(text)
index = []
for i in range(len(text)):
    if text[i] == text[0]:
        index.append(i)
print(index)

number = []
max = 0
for i in range(2, index[-1]):
    if index[-1] % i == 0:
        number.append(i)
print(number)






file = open("OUTPUT.TXT", "w")
#file.write(otvet)
file.close()

