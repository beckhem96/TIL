def BFS1():
    ci, cj = start.pop(0)
    return BFS2(ci, cj)
def BFS2(ci, cj):
    global result
    v = [[0] * 5 for _ in range(5)]
    q = [(ci, cj)]
    v[ci][cj] = 1
    cnt = 0
    while q:
        i, j = q.pop(0)
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and not v[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
                if arr[ni][nj] == 2 and result > cnt:
                    result = cnt
                    return result
arr = [[1, 0, 0, 3, 0], [1, 1, 1, 3, 0], [1, 0, 3, 3, 0], [0, 0, 0, 2, 2], [0, 0, 0, 0, 2]]
start = []
for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            start.append((i, j))
result = 1000
print(BFS1())