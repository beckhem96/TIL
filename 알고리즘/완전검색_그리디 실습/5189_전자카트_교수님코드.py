import sys

sys.stdin = open('5189_전자카트.txt', 'r')

def nPr(i, N):
    global minV

    if i==N:
        s = 0                   # 배터리사용량
        for j in range(1, N):
            s += arr[p[j-1]][p[j]]      # 이동 지역 사이의 비용
        s += arr[p[N-1]][0]     # 마지막 관리지역에서 사무실로 오는 비용
        if minV > s:
            minV = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            nPr(i+1, N)
            p[i], p[j] = p[j], p[i]


    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    minV = 1000000
    nPr(1, N)
    print(f'#{tc} {minV}')