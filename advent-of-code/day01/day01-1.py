with open("day1.txt", "r") as f:
    data = f.read()
data = data.split("\n")

elf = 0
mx = 0

for i in data:
    if i == "":
        mx = elf if elf > mx else mx
        elf = 0

    elif i.isnumeric():
        elf += int(i)

    else: raise ValueError()


print(mx)

