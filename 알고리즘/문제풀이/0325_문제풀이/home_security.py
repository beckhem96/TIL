T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    homes = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                homes.append([i, j])
    res = 0
    for k in range(1, N+2):
        cost = k*k+(k-1)*(k-1)
        for si in range(N):
            for sj in range(N):
                cnt = 0
                for i, j in homes:
                    if abs(i-si)+abs(j-sj) < k:
                        cnt += 1
                if cnt*M-cost >= 0:
                    if res < cnt:
                        res = cnt
    print(f'#{tc} {res}')