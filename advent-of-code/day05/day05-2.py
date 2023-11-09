from numpy import array, transpose
from re import search

stack = []
with open("day5.txt", "r") as f:
    for i in range(9): stack.append(f.readline())
    f.readline()
    steps = f.read()[:-1].split("\n")


stack = stack[::-1]
for i in range(len(stack)):
    stack[i] = [stack[i][4*j: 4*(j+1)].strip() for j in range(9)]
stack = transpose(array(stack))
stack = {i[0]: " ".join(list(i[1:])).split() for i in stack}


for i in range(len(steps)):
    t = search(r"move (\d+) from (\d+) to (\d+)", steps[i])
    steps[i] = (int(t.group(1)), t.group(2), t.group(3))


for i in steps:
    (n, src, dst) = i
    n = min(n, len(stack[src]))
    stack[dst].extend(stack[src][-n:])
    stack[src] = stack[src][:-n]
    print(n, stack[src])

[print(stack[i][-1].replace("[", "").replace("]", ""), end="") for i in stack]
print()

