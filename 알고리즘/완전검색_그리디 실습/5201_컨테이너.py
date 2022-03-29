import sys

sys.stdin = open('5201_컨테이너.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    weight.sort()
    truck.sort()
    result = 0
    n, m = N-1, M-1
    i = min(n, m)
    while n >= 0 and m >= 0:
        if weight[n] <=truck[m]:
            result += weight[n]
        else:
            n -= 1
            continue
        n -= 1
        m -= 1

    print(f'#{tc} {result}')