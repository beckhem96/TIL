# 3
# 5
# 2 2 1 1 3
# 10
# 7 5 4 1 2 10 3 6 9 8
# 100
# 158 56 163 106 108 153 159 147 93 140 126 9 145 166 191 106 48 183 184 115 197 136 45 196 175 89 199 52 186 170 199 28 190 40 83 48 151 35 128 4 13 38 65 20 76 142 23 63 30 30 178 36 32 114 79 68 2 187 106 98 67 131 109 177 20 113 1 102 172 119 197 190 28 82 165 168 60 18 156 174 78 42 110 63 56 66 191 105 72 108 104 198 179 132 99 189 183 91 28 162

def merge_sort(nums): # 분할하는 함수
    if len(nums) == 1: return nums # 분할 할게 없으면 끝
    l, r = [], []
    middle = len(nums) // 2 # 가운데 위치

    return merge(merge_sort(nums[:middle]), merge_sort(nums[middle:])) # 분할 다하면 병합

def merge(l, r): # 병합하는 함수
    global cnt
    if l[-1] > r[-1]:
        cnt += 1

    result = []
    i, j = 0, 0
    while len(l) > i or len(r) > j: # 둘 중에 하나가 안쓴 값이 있는데
        if len(l) > i and len(r) > j: # 두 리스트 둘 다 안쓴값이 있으면
            if l[i] <= r[j]: # 오른쪽 첫 번째 값이 더 크면
                result.append(l[i]) # 왼쪽 리스트 첫 번쨰 값을 result에 넣어줌
                i += 1
            else:
                result.append(r[j]) # 아니면 반대
                j += 1
        elif len(l) > i:
            result.append(l[i]) # l에만 안쓴 값있을때
            i += 1
        elif len(r) > j:
            result.append(r[j]) # r에만 안쓴 값 있을 떄
            j += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(nums)[N//2]} {cnt}')

