def line(x1, y1, x2, y2):
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)  ** 0.5
    return d

def plGeron(A, B, C):
    p = (A + B + C) / 2
    S = (p * (p - A) * (p - B) * (p - C)) ** 0.5
    return S

def test(cel):
    global countDebil
    X = int(cel[0])
    Y = int(cel[1])

    X1 = int(cel[2])
    Y1 = int(cel[3])

    X2 = int(cel[4])
    Y2 = int(cel[5])

    X3 = int(cel[6])
    Y3 = int(cel[7])

    X4 = int(cel[8])
    Y4 = int(cel[9])

    a = line(X1, Y1, X2, Y2)
    b = line(X2, Y2, X3, Y3)
    c = line(X3, Y3, X4, Y4)
    d = line(X4, Y4, X1, Y1)

    Spr = min(a, b, c, d) * max(a, b, c, d)

    a1 = line(X, Y, X1, Y1)
    b1 = line(X, Y, X2, Y2)
    c1 = line(X1, Y1, X2, Y2)

    a2 = line(X, Y, X3, Y3)
    b2 = line(X, Y, X2, Y2)
    c2 = line(X3, Y3, X2, Y2)

    a3 = line(X, Y, X3, Y3)
    b3 = line(X, Y, X4, Y4)
    c3 = line(X3, Y3, X4, Y4)

    a4 = line(X, Y, X1, Y1)
    b4 = line(X, Y, X4, Y4)
    c4 = line(X1, Y1, X4, Y4)

    Str1 = plGeron(a1, b1, c1)
    Str2 = plGeron(a2, b2, c2)
    Str3 = plGeron(a3, b3, c3)
    Str4 = plGeron(a4, b4, c4)

    #print(abs(Str1 + Str2 + Str3 + Str4 - Spr))
    #print(round(Str1 + Str2 + Str3 + Str4, 3), round(Spr, 3))
    if abs(Str1 + Str2 + Str3 + Str4 - Spr) >=0 and abs(Str1 + Str2 + Str3 + Str4 - Spr) <= 0.2:
        countDebil += 1



text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])

n = int(text[0])
del(text[0])

people = []
for cel in text:
    people.append(cel.split(" "))

countDebil = 0
for debil in people:
    test(debil)


file = open("OUTPUT.TXT", "w")
file.write(str(countDebil))
file.close()
