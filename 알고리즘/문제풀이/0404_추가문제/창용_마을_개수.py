def search(n, v):
    if v[relation[i*2+1]] != 0:
        return
    elif v[relation[i*2+1]] == 0:
        search(relation[i*2+1], v[relation[i*2+1]] + 1)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    relation = []
    for _ in range(M):
        a, b = map(int, input().split())
        relation.append(a)
        relation.append(b)
    cnt = 1
    v = [0] * (N+1)
    for i in range(M):
        search(relation[i*2], v)

    print(v)