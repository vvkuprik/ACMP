text =  open("INPUT.TXT", "r").read().split("\n")[0].split(" ")

a = text[0]
b = text[1]

count1 = 0
count2 = 0

for i in range(4):
    if a[i] == b[i]:
        count1 += 1
    elif a[i] in b:
        count2 += 1


file = open("OUTPUT.TXT", "w")
file.write(str(count1) +" "+ str(count2))
file.close()

