with open("day9.txt", "r") as f:
    data = [i.split() for i in f.read().split("\n")[:-1]]


xy = [[0, 0]]*10
tail = set()


def update_head(hx, hy, d):
    
    if d == "U": hy += 1
    elif d == "D": hy -= 1
    elif d == "R": hx += 1
    elif d == "L": hx -= 1
    
    return [hx, hy]

def update_tail(tx, ty, hx, hy):

    if abs(tx-hx) <= 1 and abs(ty-hy) <= 1:
        tx, ty = tx, ty
    
    elif (hy==ty) and abs(hx-tx)==2:
        tx += (hx-tx)//2
    elif (hx==tx) and abs(hy-ty)==2:
        ty += (hy-ty)//2

    elif abs(hx-tx)==1 and abs(hy-ty)==2:
        tx += (hx-tx)
        ty += (hy-ty)//2
    elif abs(hy-ty)==1 and abs(hx-tx)==2:
        ty += (hy-ty)
        tx += (hx-tx)//2
    
    elif abs(hx-tx)==2 and abs(hy-ty)==2:
        tx += (hx-tx)//2
        ty += (hy-ty)//2
    elif abs(hy-ty)==2 and abs(hx-tx)==2:
        ty += (hy-ty)//2
        tx += (hx-tx)//2
    return [tx, ty]


for i in data:
    for j in range(int(i[1])):
        xy[0] = update_head(xy[0][0], xy[0][1], i[0])
        for k in range(1, 10):
            xy[k] = update_tail(xy[k][0], xy[k][1], xy[k-1][0], xy[k-1][1])
        tail.add(tuple(xy[9]))

print(len(tail))

