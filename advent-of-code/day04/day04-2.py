with open("day4.txt" ,"r") as f:
    data = f.read()[:-1]

data = data.split("\n")
data = [i.split(",") for i in data]


ct = 0
for i in data:

    al, ar = (int(j) for j in i[0].split("-"))
    bl, br = (int(j) for j in i[1].split("-"))

    if (ar >= bl) and (br >= al):
        ct += 1
        print(i, ct)

print(ct)

