text =  open("INPUT.TXT", "r").read().split("\n")
if text[-1] == "":
    del(text[-1])
ticket = text[0]

otvet = "NO"

if len(ticket) > 1:

    for i in range(1, len(ticket)):
        if otvet == "YES":
            break

        sumLeft = 0
        sumRight = 0

        for symbol in ticket[:i]:
            sumLeft += int(symbol)
        for symbol in ticket[i:]:
            sumRight += int(symbol)


        while sumLeft > 9:
            newTicket = str(sumLeft)
            sumLeft = 0
            for i in newTicket:
                sumLeft += int(i)

        while sumRight > 9:
            newTicket = str(sumRight)
            sumRight = 0
            for i in newTicket:
                sumRight += int(i)



        if sumLeft == sumRight:
            otvet = "YES"



file = open("OUTPUT.TXT", "w")
file.write(otvet)
file.close()

