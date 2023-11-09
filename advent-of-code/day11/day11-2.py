from types import FunctionType
import re


with open("day11/day11-test.txt") as f:
    data = [i.split("\n") for i in f.read().split("\n\n")]


class Monkey:

    def __init__(self, data):
        self.data = data
        self.inspects = 0
        self.parser()
    
    def parser(self):
        self.name = int(re.findall(r'\d+', self.data[0])[0])
        self.items = [float(i) for i in re.findall(r'\d+', self.data[1])]
        self.operation = eval(f"lambda old: {re.search(r'= (.*)', self.data[2]).group(1)}")
        div = int(re.findall(r'\d+', self.data[3])[0])
        self.divisibility = lambda x: int(bool(x % div))
        m1 = int(re.findall(r'\d+', self.data[4])[0])
        m2 = int(re.findall(r'\d+', self.data[5])[0])
        self.nextmonkey = (m1, m2)

monkeys = []
for i in range(len(data)):
    monkeys.append(Monkey(data[i]))
print(len(monkeys))


for rounds in range(1_000):
    if not rounds % 100: print(rounds, "rounds")

    for monkey in monkeys:

        for item in monkey.items:

            item = monkey.operation(item)
            # item = item // 3
            monkeys[monkey.nextmonkey[monkey.divisibility(item)]].items.append(item)
            monkey.inspects += 1
        
        monkey.items = []

[print(i.items) for i in monkeys]

inspects = [i.inspects for i in monkeys]
inspects = sorted(inspects)
print(inspects[-1], inspects[-2], inspects)

