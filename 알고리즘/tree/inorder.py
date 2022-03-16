# def in_order(v):
#     if v:
#         in_order(ch1[v])
#         print(key_value[v], end='')
#         in_order(ch2[v])
# for tc in range(1, 11):
#     N = int(input())
#     arr = [list(input().split()) for _ in range(N)]
#     arr_tree = []
#     key_value = dict()
#     for i in range(len(arr)):
#         key_value[int(arr[i][0])] = arr[i][1]
#     for i in range(N):
#         for j in range(2, 4):
#             if j<len(arr[i]):
#                 arr_tree.append(int(arr[i][0]))
#                 arr_tree.append(int(arr[i][j]))
#     ch1 = [0]*(N+1)
#     ch2 = [0]*(N+1)
#     E = N - 1
#     for i in range(E): # 부모-자식 E개의 쌍이 주어진 상태
#         p, c = arr_tree[i*2], arr_tree[i*2+1]
#         if ch1[p] == 0: # 아직 자식이 없는 경우
#             ch1[p] = c
#         else:
#             ch2[p] = c
#     print(f'#{tc} ', end='')
#     in_order(1)
#     print()

# 한상우님 코드 # 이진 트리라 가능한 탐색임
def f(v):
    if v <= N:
        f(v * 2)
        print(t[v], end='')
        f(v * 2 + 1)


# for tc in range(1, 11):
N = int(input())
t = [0] * (N + 1)
for i in range(N):
    a = input().split()
    t[int(a[0])] = a[1]
print(t)
# print(f'#{tc}', end=' ')
# f(1)
# print()

