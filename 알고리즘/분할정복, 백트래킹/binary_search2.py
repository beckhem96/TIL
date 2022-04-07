import sys

sys.stdin = open('binary_search.txt', 'r')

def binary_search(arr, l, r, key, check): # 재귀
    if l > r:
        return
    else:
        mid = (l+r) // 2
        if key == arr[mid]:
            return 1
        elif key < arr[mid]:
            if check == 1:
                return
            check = 1
            return binary_search(arr, l, mid - 1, key, check)
        else:
            if check == 2:
                return
            check = 2
            return binary_search(arr, mid + 1, r, key, check)



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
        if binary_search(A, 0, N-1, n, 0):
            result += 1
    print(f'#{tc} {result}')