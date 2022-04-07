di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, n, ans):
    if n == 6:
        sol.add(ans)
        return
    # for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
    #     ni, nj = i+di, j+dj
    #     if 0<=ni<4 and 0<=nj<4:
    #         dfs(ni, nj, n+1, ans+arr[ni][nj])
    for k in range(4):
        nx = i + di[k]
        ny = j + dj[k]
        if 0<=nx < 4 and 0<=ny < 4:
            dfs(nx, ny, n+1, ans+arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sol = set()
    for si in range(4):
        for sj in range(4):
            dfs(si, sj, 0, arr[si][sj])
    print(f'#{tc} {len(sol)}')