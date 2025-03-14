text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

n = int(text[0])

kvartira = -1
years = -1

for i in range(1, len(text)):
    people = text[i].split(" ")
    print(people)
    if people[1] == "1":
        if int(people[0]) > years:
            years = int(people[0])
            kvartira = i

file = open("OUTPUT.TXT", "w")
file.write(str(kvartira))
file.close()

