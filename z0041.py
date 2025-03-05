text = open("INPUT.TXT", "r").read().split("\n")[1]

MS = [int(i) for i in text.split()]
MS.sort()


file = open("OUTPUT.TXT", "w")
file.write(" ".join([str(i) for i in MS]))
file.close()
