with open("day1.txt", "r") as f:
    data = f.read()
data = data.split("\n")

# print(data)


elf = 0
mx = [0]*3

for i in data:
    if i == "":
        idx = 3 - sum([elf > j for j in mx])
        mx.insert(idx, elf)
        mx.pop()
        elf = 0

    elif i.isnumeric():
        elf += int(i)

    else: raise ValueError()


print(sum(mx))

