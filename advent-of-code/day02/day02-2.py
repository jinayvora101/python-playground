with open("day2.txt", "r") as f:
    data = f.read()
    data = data[:-1]

data = [i.split(" ") for i in data.split("\n")]

wl_map = [None, 3, 1, 2]
myscore = 0

for i in data:
    
    opp = ord(i[0]) - 64
    res = ord(i[1]) - 87
    temp = (res - 1) * 3
    
    if res == 1: temp += wl_map[opp]
    elif res == 2: temp += opp
    elif res == 3: temp += wl_map.index(opp)
    
    myscore += temp

print(myscore)

