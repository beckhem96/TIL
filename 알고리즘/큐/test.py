def maze(q):
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if arr[ni][nj] == 3:
                return 1
            elif 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj))
    return 0
for _ in range(10):
    N = 16
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    q = []
    starti, startj = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                starti, startj = i, j

    q.append((starti, startj))
    print(f'#{tc} {maze(q)}')
