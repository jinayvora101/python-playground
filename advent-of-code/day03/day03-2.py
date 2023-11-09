with open("day3.txt", "r") as f:
    data = f.read()

data = data.split("\n")


unarr = []
n = len(data)

for i in range(len(data)//3):
    t = data[3*i: 3*i+3]
    for j in t[0]:
        if j in t[1] and j in t[2]:
            s = ord(j)-64+26 if ord(j)<91 else ord(j)-96
            unarr.append(s)
            break

print(sum(unarr))
# print(sum(unarr[:, 0]))

