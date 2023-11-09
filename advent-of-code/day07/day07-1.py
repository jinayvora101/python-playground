class node:

    def __init__(self, name, parent, is_folder=True, size=0):
        self.name = name
        self.parent = parent
        self.is_folder = is_folder
        self.child = {} if is_folder else None
        self.size = size

    def set_child(self, name, child):
        self.child[name] = child
        self.update_size(child.size)

    def update_size(self, size):
        self.size += size
        if self.name != "/": self.parent.update_size(size)

    def __str__(self):
        return f"""-------------------------
Name: {self.name} - {"folder" if self.is_folder else "file"}
Parent: {self.parent.name}
Child: {[self.child[i].name for i in self.child] if self.is_folder else "NA"}
Size: {self.size}"""


with open("day7.txt", "r") as f:
    data = f.read().split("$")[1:]

for i in range(len(data)):
    x = data[i].strip().split("\n")
    data[i] = [x.pop(0).split(), x]


root = node("/", None)
root.parent = root

curr = root

for i in data:
    if i[0][0] == "cd":
        if i[0][1] == "/": curr = root
        elif i[0][1] == "..": curr = curr.parent
        else: curr = curr.child[i[0][1]]

    elif i[0][0] == "ls":
        for j in i[1]: 
            [typ, name] = j.split()
            if typ == "dir":
                tmp = node(name, curr)
                curr.set_child(name, tmp)
            elif typ.isnumeric():
                tmp = node(name, curr, False, int(typ))
                curr.set_child(name, tmp)


def return_size_cum(root):

    if not root.is_folder: return 0

    s = 0
    if root.size <= 100_000:
        s = root.size
    
    if not root.is_folder:
        return s
    
    for i in root.child:
        s += return_size_cum(root.child[i])

    return s

print(return_size_cum(root))

