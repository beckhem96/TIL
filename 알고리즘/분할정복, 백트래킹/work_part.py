import sys

sys.stdin = open('work_part.txt', 'r')
def f(i, n, s):
    global result
    if i == n:
        if result < s:
            result = s
    elif result >= s:
        return
    else:
        for j in range(n):
            if not v[j]:
                v[j] = 1
                f(i + 1, n, s*arr[i][j]/100)
                v[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0] * N
    result = 0
    f(0, N, 1)
    print(f'#{tc}{result*100 : .6f}')