text =  open("INPUT.TXT", "r").read().split("\n")
numer = text[0].split(" ")

for i in range(3):
    numer[i] = int(numer[i])


mn = min(numer)
mx = max(numer)

file = open("OUTPUT.TXT", "w")
file.write(str(mx - mn))
file.close()
