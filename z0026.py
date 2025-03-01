text =  open("INPUT.TXT", "r").read().split("\n")
circle1 = text[0].split(" ")
circle2 = text[1].split(" ")



d = (((int(circle1[0]) - int(circle2[0])) ** 2) + ((int(circle1[1]) - int(circle2[1])) ** 2) ) ** 0.5


file = open("OUTPUT.TXT", "w")
if int(circle1[2]) + int(circle2[2]) >= d and d >= abs(int(circle1[2]) - int(circle2[2])):
    file.write("YES")
else:
    file.write("NO")
file.close()
