text =  open("INPUT.TXT", "r").read().split("\n")
text1 = text[0]
text2 = text[1]

counter = 0
for i in range(len(text2)):
    j = 0
    while j < len(text1) - len(text2) + 1:
        if text1[j: j + len(text2)] == text2[i:] + text2[:i]:
            counter += 1
            j+=len(text2)
        else:
            j += 1
    #counter += text1.count(text2[i:] + text2[:i])


file = open("OUTPUT.TXT", "w")
file.write(str(counter))
file.close()
