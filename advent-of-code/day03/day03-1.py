with open("day3.txt", "r") as f:
    data = f.read()

def bisect(x):
    n = len(x)
    return (x[:n//2], x[n//2:])

data = [bisect(i) for i in data.split("\n")]
print(data)


unarr = []

for i in data:
    for j in i[0]:
        if j in i[1]:
            t = ord(j)-64+26 if ord(j)<91 else ord(j)-96
            unarr.append(t)
            break

print(sum(unarr))

