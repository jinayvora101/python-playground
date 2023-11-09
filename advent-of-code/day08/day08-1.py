import numpy as np

with open("day8/day8.txt") as f:
    data = [list(i) for i in f.read().split("\n")[:-1]]

data = np.array(data).astype(np.uint8)


def check_hidden(arr, x):
    return max(arr) >= x


total_ct = np.product(data.shape)
visible_ct = (np.sum(data.shape) * 2) - 4
hidden_ct = 0

for i in range(1, data.shape[0]-1):
    for j in range(1, data.shape[1]-1):

        if not (check_hidden(data[i, :j], data[i, j]) and \
                check_hidden(data[i, j+1:], data[i, j]) and \
                check_hidden(data[:i, j], data[i, j]) and \
                check_hidden(data[i+1:, j], data[i, j])):
                   visible_ct += 1

        else: hidden_ct += 1


print(visible_ct + hidden_ct == total_ct)
print(visible_ct)

