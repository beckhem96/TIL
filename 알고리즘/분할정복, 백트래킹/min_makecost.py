import sys

sys.stdin = open('min_makecost.txt', 'r')

def f(i, n, sumV):
    global result
    if i == n:
        if result > sumV:
            result = sumV
    elif result < sumV:
        return
    else:
        for j in range(n):
            if not v[j]:
                v[j] = 1
                f(i+1, n, sumV+arr[i][j])
                v[j] = 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    result = N*99
    f(0, N, 0)
    print(f'#{tc} {result}')
