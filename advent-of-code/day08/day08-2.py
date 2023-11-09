import numpy as np

with open("day8/day8.txt") as f:
    data = [list(i) for i in f.read().split("\n")[:-1]]

data = np.array(data).astype(np.uint8)


def block_dist(arr, x):
    for idx, i in enumerate(arr):
        if i >= x:
            break
    return idx + 1


score = []

for i in range(1, data.shape[0]-1):
    for j in range(1, data.shape[1]-1):

        score.append( \
            block_dist(np.flip(data[i, :j]), data[i, j]) * \
            block_dist(data[i, j+1:], data[i, j]) * \
            block_dist(np.flip(data[:i, j]), data[i, j]) * \
            block_dist(data[i+1:, j], data[i, j]) \
            )


print(max(score))

