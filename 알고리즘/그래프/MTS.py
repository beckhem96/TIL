
def find_set(i):
    while p[i] != i:# i가 자기 자신을 가리킬 때 까지
        i = p[i]     # 따라가보기
    return i


def union(n1, n2):
    p[find_set(n2)] = find_set(n1)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge.append((w, n1, n2))
    # Kruskal
    edge.sort() # 가중치 기준 오름차순  정렬
    p = [i for i in range(V+1)] # 대표원소
    cnt = 0 # 선택한 간선수
    s = 0 # MST에 속한 간선

    for w, n1, n2 in edge:# V개의 간선 선택
        if find_set(n1) != find_set(n2):# 사이클이 아니면
            s += w # MST의 가중치 추가
            union(n1, n2)
            cnt += 1
            if cnt == V:# MST완성
                break
    print(f'#{tc} {s}')
# def find_set(i):
#     while p[i] != i:
#         i = p[i]
#     return i
#
#
# def union(n1, n2):
#     p[find_set(n2)] = find_set(n1)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     edge = []
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         edge.append((w, n1, n2))
#
#     # Kruskal
#     edge.sort()
#     p = [i for i in range(V + 1)]
#     cnt = 0
#     s = 0
#     for w, n1, n2 in edge:
#         if find_set(n1) != find_set(n2):
#             s += w
#             union(n1, n2)
#             cnt += 1
#             if cnt == V:
#                 break
#
#     print(f'#{tc} {s}')
