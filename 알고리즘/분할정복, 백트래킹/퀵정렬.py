import sys

sys.stdin = open('퀵정렬.txt', 'r')

def partition(nums, l, r):
    p = l
    i, j = l+1, r
    while i <= j:
        while i <= r and nums[i] <= nums[p]:
            i += 1
        while j > l and nums[j] >= nums[p]:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            nums[j], nums[p] = nums[p], nums[j]
    return j

def quicksort(nums, l, r):
    if l >= r:
        return
    else:
        s = partition(nums, l, r) # pivot 위치 반환

        quicksort(nums, l, s-1) # pivot왼쪽
        quicksort(nums, s+1, r) # 오른쪽

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    quicksort(nums, 0, N-1)
    print(f'#{tc}', nums[N//2])

