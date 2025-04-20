import sys
sys.set_int_max_str_digits(6680)
text = open("INPUT.TXT", "r").read().split("\n")[0].split()
otvet = int(text[0]) ** int(text[1])


file = open("OUTPUT.TXT", "w")
file.write(str(otvet))
file.close()
