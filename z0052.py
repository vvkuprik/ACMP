text =  open("INPUT.TXT", "r").read().split("\n")

if text[-1] == "":
    del(text[-1])


number = text[0]



file = open("OUTPUT.TXT", "w")
if int(number[0]) + int(number[1]) + int(number[2]) == int(number[-1]) + int(number[-2]) + int(number[-3]):
    file.write("YES")
else:
    file.write("NO")
file.close()

