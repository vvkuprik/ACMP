text =  open("INPUT.TXT", "r").read().split("\n")
str_time = text[0].split(":")
end_time = text[1].split(":")

final_time = [0, 0, 0]

otvet = ""


if len(end_time) < 3:
    end_time.reverse()
    for i in range(3-len(end_time)):
        end_time.append(0)
    end_time.reverse()


for i in range(3):
    end_time[i] = int(end_time[i])
    str_time[i] = int(str_time[i])

for i in range(3):
    final_time[i] = int(str_time[i]) + int(end_time[i])


if final_time[-1] >= 60:
    final_time[-2] += final_time[-1] // 60
    final_time[-1] %= 60

if final_time[-2] >= 60:
    final_time[-3] += final_time[-2] // 60
    final_time[-2] %= 60

days = 0
if final_time[-3] >= 24:
    days = final_time[-3] // 24
    final_time[-3] %= 24



message = ""
for i in range(len(final_time)):
    message += (2-len(str(final_time[i]))) * "0"
    message += str(final_time[i])
    if i == 2 and days > 0:
        message += "+"
        message += str(days)
        message += " days"
    elif i == 2 and days == 0:
        pass
    else:
        message += ":"


file = open("OUTPUT.TXT", "w")
file.write(message)
file.close()

