with open("day10.txt", "r") as f:
    data = f.read()

data = [i.split() for i in data.split("\n")[:-1]]


crt = ["."]*(40*6)
x = 1
ptr = 0

while ptr < 240:
    if abs(ptr-x) <= 1:
        crt[ptr] = "#"
    print(ptr, [x-1, x, x+1])
    ptr += 1

    if (ptr+1)%40 == 0: x += 40

    if data[0][0] == "addx":
        if abs(ptr-x) <= 1:
            crt[ptr] = "#"
        print(ptr, [x-1, x, x+1])
        ptr += 1
        x += int(data[0][1])
        if (ptr+1)%40 == 0: x += 40


    data.pop(0)

for idx, i in enumerate(crt):
    print(i, end=" ")
    if (idx+1)%40 == 0: print()

