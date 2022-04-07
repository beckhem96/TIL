import sys

sys.stdin = open('1000000_number.txt', 'r')

# def partition(nums, l, r):
#     p = nums[l]
#     i, j = l, r
#     while i <= j:
#         while i <= j and nums[i] <= p:
#             i += 1
#         while i <= j and nums[j] >= p:
#             j -= 1
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#
#     nums[l], nums[j] = nums[j], nums[l]
#     return j

def quicksort(nums, l, r):
    if l < r:
        # 위치반환
        p = nums[l]
        i, j = l, r
        while i <= j:
            while i <= j and nums[i] <= p:
                i += 1
            while i <= j and nums[j] >= p:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[l], nums[j] = nums[j], nums[l]

        quicksort(nums, l, j-1) # pivot왼쪽
        quicksort(nums, j+1, r) # 오른쪽


N = 1000000
nums = list(map(int, input().split()))
quicksort(nums, 0, N-1)
print(nums[500000])
