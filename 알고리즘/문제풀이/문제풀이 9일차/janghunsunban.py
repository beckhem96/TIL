# def f(i, n, k):
#     if i == n: # 드디어 bit 다 채웠어
#         print(bit)
#         s = 0
#         for j in range(n):
#             if bit[j]: # 부분집합의 원소들을 더해주는 과정
#                 s += a[j]
#         if s == k: # 그 합이 k와 같다면? 그 부분집합 출력해주는 과정
#             for j in range(n):
#                 if bit[j]:
#                     print(a[j], end=' ')
#             print()
#     else:
#         bit[i] = 1   # 1을 하나씩 넣어주고
#         # print('첫번째', bit, f'f({i})')
#         f(i+1, n, k)  # i == n 되면 if 실행후
#         bit[i] = 0    # 0으로 하나씩 바꿔줌
#         # print('두번쨰', bit, f'f({i})')
#         f(i+1, n, k)  # 그리고 i == n 될 떄까지 반복해서 f(0)으로 돌아와서 return
#     return
#
# N = 4
# a = list(range(1, N+1))
# bit = [0]*N
# K = 10
# f(0, N, K) # 합이 K인 부분집합을 찾는 함수

def f(i, n, k):
    if i == n:
        s = 0
        for j in range(n):
            if bit[j]:
                s += arr[j]
        if s >= k:
            result.append(s)
    else:
        bit[i] = 1
        f(i+1, n, k)
        bit[i] = 0
        f(i+1, n, k)
    return

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    bit = [0] * N
    result = []
    f(0, N, B)

    print(f'#{tc} {min(result) - B}')