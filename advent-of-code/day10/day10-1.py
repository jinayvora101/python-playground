with open("day10.txt", "r") as f:
    data = f.read()

data = [i.split() for i in data.split("\n")[:-1]]


t = [1]

for i in data:
    if i[0] == "noop":
        t.append(t[-1])

    elif i[0] == "addx":
        t.extend([t[-1], t[-1] + int(i[1])])

sum = 0
for i in [20, 60, 100, 140, 180, 220]:
    sum += i*t[i-1]
    print(i, t[i-1])

print(sum)

