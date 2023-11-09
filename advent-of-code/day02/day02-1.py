with open("day2.txt", "r") as f:
    data = f.read()
    data = data[:-1]

data = [i.split(" ") for i in data.split("\n")]

myscore = 0
for i in data:
    
    opp = ord(i[0]) - 64
    you = ord(i[1]) - 87
    temp = you

    if you == opp: temp += 3
    elif (you-opp)%3 == 1: temp += 6

    myscore += temp

print(myscore)

