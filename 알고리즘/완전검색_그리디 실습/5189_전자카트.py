import sys

sys.stdin = open('5189_전자카트.txt', 'r')

def perm(n, k):
    global minV
    if n == k:
        a = [0] + p + [0]
        result = 0
        for i in range(len(a)-1):
            result += arr[a[i]][a[i+1]]
        minV = min(minV, result)

    else:
        for i in range(k):
            if used[i] == 0:
                p[n] = num[i]
                used[i] = 1
                perm(n+1, k)
                used[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = N-1
    num = []
    for i in range(1, N):
        num.append(i)
    p = [0]*k
    used = [0]*k
    minV = 123456789
    perm(0, k)
    print(f'#{tc} {minV}')
