
def new_round(number, count):
    number = str(number).split(".")
    if len(number) == 1:
        number = number[0]
        return number
    else:
        if int(number[1][0]) >= 5:
            number = int(number[0]) + 1
        else:
            number = int(number[0])
    return number

text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])
n = int(text[0])
del(text[0])

trains = []
for _ in range(n):
    rain = text[0].split()
    del(text[0])

    count = 0
    for j in range(len(rain)):

        if chr(34) in rain[j]:
            count = j


    name = " ".join(rain[0:count+1])
    temp = [name[:]]
    for k in range(count+1, len(rain)):
        temp.append(rain[k])

    trains.append(temp[:])

number_train = -1
speed_tran = -1

for i in range(len(trains)):
    temp = trains[i][-1].split(":")
    final_time = int(temp[0]) * 60 + int(temp[1])
    temp = trains[i][-2].split(":")
    start_time = int(temp[0]) * 60 + int(temp[1])

    if final_time <= start_time:
        final_time += 24*60

    time = final_time - start_time

    if speed_tran == -1:
        number_train = i
        speed_tran = 650 / (time / 60)
    elif speed_tran < 650 / (time / 60):
        number_train = i
        speed_tran = 650 / (time / 60)

name_train = trains[number_train]


file = open("OUTPUT.TXT", "w")
file.write("The fastest train is ")
file.write(name_train[0])
file.write(".\n")
file.write("Its speed is ")
file.write(str(new_round(speed_tran, 0)))
file.write(" km/h, approximately.")
file.close()

