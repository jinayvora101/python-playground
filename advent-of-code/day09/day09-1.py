with open("day9.txt", "r") as f:
    data = [i.split() for i in f.read().split("\n")[:-1]]


hx, hy = 0, 0
tx, ty = 0, 0
tail = set()


def update_head(hx, hy, d):
    
    if d == "U": hy += 1
    elif d == "D": hy -= 1
    elif d == "R": hx += 1
    elif d == "L": hx -= 1
    
    return hx, hy

def update_tail(tx, ty, hx, hy):

    if abs(tx-hx) <= 1 and abs(ty-hy) <= 1: tx, ty = tx, ty
    
    elif (hy==ty) and abs(hx-tx)==2: tx += (hx-tx)//2
    elif (hx==tx) and abs(hy-ty)==2: ty += (hy-ty)//2
    
    elif abs(hx-tx)==1 and abs(hy-ty)==2:
        tx += (hx-tx)
        ty += (hy-ty)//2
    elif abs(hy-ty)==1 and abs(hx-tx)==2:
        ty += (hy-ty)
        tx += (hx-tx)//2

    return tx, ty


for i in data:
    for j in range(int(i[1])):
        hx, hy = update_head(hx, hy, i[0])
        tx, ty = update_tail(tx, ty, hx, hy)
        tail.add((tx, ty))

print(len(tail))

