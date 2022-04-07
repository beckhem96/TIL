import sys

sys.stdin = open('binary_search.txt', 'r')

# def binary_search(check, arr, num):
#     global result
#     if len(arr) == 1 and arr[0] == num: # 종료조건
#         return 1
#     else:
#         mid = len(arr)//2
#         l = arr[:mid] # 왼쪽
#         r = arr[mid+1:] # 오른쪽
#         if arr[mid] < num: # 중앙보다 큰수
#             if check == 1:
#                 return 0
#             result += 1
#             check = 1
#             binary_search(check, r, num)
#         elif arr[mid] > num: # 중앙보다 작은 수
#             if check == 2:
#                 return 0
#             result += 1
#             check = 2
#             binary_search(check, l, num)

def binary_search(n, arr, key, check): # 반복구조
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] > key:
            if check == 1:
                return
            check = 1
            r = mid - 1
        else:
            if check == 2:
                return
            check = 2
            l = mid + 1
    return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0 # 조건에 맞는 수
    A.sort()
    B.sort()
    result = 0
    for n in B:
        if binary_search(N, A, n, 0):
            result += 1
    print(f'#{tc} {result}')

