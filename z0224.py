text =  open("INPUT.TXT", "r").read().split("\n")[1].split()



MS = [int(i) for i in text]

MS.sort()

otvet = MS[-1] * MS[-2] * MS[-3]
new_otvet = MS[0] * MS[1] * MS[-1]
if otvet < new_otvet:
    otvet = new_otvet

file = open("OUTPUT.TXT", "w")
file.write(str(otvet))

file.close()

