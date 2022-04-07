def BFS(ci, cj):
    global cnt
    q = [(ci, cj)]
    v[ci][cj] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0<=ni<6 and 0<=nj<4 and not v[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
                if arr[ni][nj] == 2:
                    return cnt
                
arr = [[0,1,0,0], [0,1,2,2], [0,1,0,2], [0,1,0,2], [0,0,0,0],[0,0,0,0]]
v = [[0] * 4 for _ in range(6)]
cnt = 0
print(BFS(1, 0))