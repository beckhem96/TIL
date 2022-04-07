import sys

sys.stdin = open('퀵정렬.txt', 'r')

def partition(nums, p, r):
    x = nums[r]
    i = p - 1

    for j in range(p, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1

def quicksort(nums, l, r):
    if l < r:
        s = partition(nums, l, r) # pivot 위치 반환

        quicksort(nums, l, s-1) # pivot왼쪽
        quicksort(nums, s+1, r) # 오른쪽

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quicksort(nums, 0, N-1)
    print(f'#{tc}', end=' ')
    print(*nums)