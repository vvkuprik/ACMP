text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

otvet = ""
if text[0] == "School" and int(text[1]) % 2 == 0:
    otvet = "No"
else:
    otvet = "Yes"



file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

