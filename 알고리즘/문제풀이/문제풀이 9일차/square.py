def f(q):
    global cnt
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == (arr[i][j]+1):
                cnt += 1
                q.append((ni, nj))
                f(q)
    return cnt




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    room_num = 0
    q = []
    result = [0]*(N*N+1)

    for i in range(N):
        for j in range(N):
            q.append((i, j))
            cnt = 1
            room_num = arr[i][j]
            f(q)
            result[room_num] = cnt
    minV = 0
    maxV = 0
    for i in range(len(result)):
        if maxV < result[i]:
            maxV = result[i]
            idx = i
    print(f'#{tc} {idx} {maxV}')


