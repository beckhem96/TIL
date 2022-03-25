arr = list(map(int, input()))
# n = 6
# dec = 0
# for x in arr:
#     dec += x*(2**n)
#     n -= 1
#     if n == 1:
#         n = 6
#         print(dec, end=' ')
#         dec = 0
result, k = 0, 0
N = len(arr)//7
for i in range(N):
    for j in range(6, -1, -1):
        if arr[i*7:i*7+7][j] == 1:
            result += 2**k
        k += 1
    print(result)
    result, k = 0, 0