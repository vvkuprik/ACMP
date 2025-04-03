text =  open("INPUT.TXT", "r").read().split("\n")


n = int(text[0].split()[0])


vagon = []
for i in text[1].split():
    if i != '':
        vagon.append(int(i))

count = 0

for i in range(n-1):
    if vagon[i] + 1 != vagon[i+1]:
        count +=1


file = open("OUTPUT.TXT", "w")
file.write(str(count))
file.close()


