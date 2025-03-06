text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])


n = int(text[0])
del(text[0])
MS1 = []

for i in range(n):
    MS1.append(text[0])
    del(text[0])

n = int(text[0])
del(text[0])
MS2 = []

for i in range(n):
    MS2.append(text[0])
    del(text[0])

MS1.sort()
MS2.sort()



file = open("OUTPUT.TXT", "w")

file.write("Friends: ")
for i in range(len(MS1)):
    file.write(MS1[i])
    if i != len(MS1) - 1:
        file.write(", ")
file.write("\n")



otevet = []
file.write("Mutual Friends: ")
for i in range(len(MS1)):
    if MS1[i] in MS2:
       otevet.append(MS1[i])
       del(MS2[MS2.index(MS1[i])])

for i in range(len(otevet)):
    file.write(otevet[i])
    if i != len(otevet) - 1:
        file.write(", ")
file.write("\n")

file.write("Also Friend of: ")
for i in range(len(MS2)):
    file.write(MS2[i])
    if i != len(MS2) - 1:
        file.write(", ")
file.write("\n")


file.close()

