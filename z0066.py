text =  open("INPUT.TXT", "r").read(1)

List = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

otvel = ""
if text == 'm':
    otvel = 'q'
else:
    for i in range(len(List)-1):
        if text == List[i]:
            otvel = List[i + 1]
            break



file = open("OUTPUT.TXT", "w")
file.write(otvel)
file.close()

