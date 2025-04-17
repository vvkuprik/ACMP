text = open("INPUT.TXT", 'r').read().split("\n")[0]
number = []
for num in text.split():
    if num.isdigit():
        number.append(int(num))

number.sort()
number_set = set(number)

flag = True
for i in range(len(number) - 1):
    if number[i] + 1 != number[i+1]:
        flag = False




if len(number_set) == 1:
    otvet = "Impossible"

elif len(number_set) == 2:
    if number.count(list(number_set)[0]) == 4 or number.count(list(number_set)[1]) == 4:
        otvet = "Four of a Kind"
    else:
        otvet = "Full House"
elif flag:
    otvet = "Straight"

elif len(number_set) == 3:
    if number.count(list(number_set)[0]) == 3 or number.count(list(number_set)[1]) == 3 or number.count(list(number_set)[2]) == 3:
        otvet = "Three of a Kind"
    else:
        otvet = "Two Pairs"
elif len(number_set) == 4:
    otvet = "One Pair"
else:
    otvet = "Nothing"

file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

