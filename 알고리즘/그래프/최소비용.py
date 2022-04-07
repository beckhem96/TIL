def f(i, j):
    q.append((i, j))
    v[i][j] = 0
    while q:
        ci, cj = q.pop(0)
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = ci+di, cj+dj

            if 0<=ni<N and 0<=nj<N:
                diff = arr[ni][nj] - arr[ci][cj] if arr[ni][nj] > arr[ci][cj] else 0
                if v[ni][nj] > v[ci][cj] + diff + 1:
                    v[ni][nj] = v[ci][cj] + diff + 1
                    q.append((ni, nj))
    return v[N-1][N-1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[1000000] * N for _ in range(N)]
    q = []
    print(f'#{tc} {f(0, 0)}')
