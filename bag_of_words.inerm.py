import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    for i, sent1 in enumerate(data):
        for j, sent2 in enumerate(data):
            if i == j:
                dist[i,j] = np.inf
            else:
                dist[i,j] = distance(sent1, sent2)
    print(np.unravel_index(np.argmin(dist), dist.shape))

def distance(row1, row2):
    sum = 0
    for i in range(len(row1)):
        sum = sum + abs(row1[i] - row2[i])
    return sum
find_nearest_pair(data)
