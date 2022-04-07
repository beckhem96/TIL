def find_set(i):
    while v[i] != i:
        i = v[i]
    return i

def union(n1, n2):
    v[find_set(n2)] = find_set(n1)



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    v = [i for i in range(N+1)]
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        n1, n2 = arr[i*2], arr[i*2+1]
        union(n1, n2)

    for i in range(1, N+1):
        if i == v[i]:
            cnt += 1
    print(f'#{tc} {cnt}')
