with open("day6.txt", "r") as f:
    data = f.read()


l, r = 0, 14
n = len(data)
print(data[l:r], n)

while r <= n:
    t = data[l:r]

    if len(set(t)) == 14:
        break

    l += 1; r += 1

print(r)

