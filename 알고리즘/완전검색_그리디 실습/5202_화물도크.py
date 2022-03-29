import sys

sys.stdin = open('5202_화물도크.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key = lambda x: (x[1], x[0]))
    k, cnt = 0, 0
    for i, j in arr:
        if i >= k:
            k = j
            cnt += 1
    print(f'#{tc} {cnt}')


